"""
Advanced ETL pipeline for NST DVA Capstone 2

This pipeline:
- Loads raw CSV
- Cleans & standardizes data
- Handles missing values
- Adds business features (churn, risk, engagement buckets)
- Validates data quality
- Exports processed dataset for Tableau & analysis
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


# -------------------------------
# STEP 1: COLUMN STANDARDIZATION
# -------------------------------

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    df = df.copy()
    df.columns = cleaned
    return df


# -------------------------------
# STEP 2: BASIC CLEANING
# -------------------------------

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)
    df = df.drop_duplicates().reset_index(drop=True)

    # Clean string columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype("string").str.strip()

    return df


# -------------------------------
# STEP 3: HANDLE MISSING VALUES
# -------------------------------

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Numeric columns → fill with median
    for col in df.select_dtypes(include="number"):
        df[col] = df[col].fillna(df[col].median())

    # Categorical → fill with "Unknown"
    for col in df.select_dtypes(include="string"):
        df[col] = df[col].fillna("Unknown")

    return df


# -------------------------------
# STEP 4: FEATURE ENGINEERING
# -------------------------------

def add_business_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Churn Flag (0/1)
    if "inactive_3_months_flag" in df.columns:
        df["churn_flag"] = df["inactive_3_months_flag"]

    # Risk Level based on skips
    if "avg_skips_per_day" in df.columns:
        df["risk_level"] = pd.cut(
            df["avg_skips_per_day"],
            bins=[-1, 10, 18, float("inf")],
            labels=["Low Risk", "Medium Risk", "High Risk"]
        )

    # Engagement Bucket
    if "engagement_score" in df.columns:
        df["engagement_bucket"] = pd.cut(
            df["engagement_score"],
            bins=[-float("inf"), 2, 4, float("inf")],
            labels=["Low", "Medium", "High"]
        )

    return df


# -------------------------------
# STEP 5: VALIDATION
# -------------------------------

def validate_data(df: pd.DataFrame) -> None:
    if "user_id" in df.columns:
        assert df["user_id"].is_unique, "❌ Duplicate user_id found!"

    if "avg_skips_per_day" in df.columns:
        assert df["avg_skips_per_day"].ge(0).all(), "❌ Negative skips detected!"

    if "engagement_score" in df.columns:
        assert df["engagement_score"].between(0, 10).all(), "❌ Invalid engagement score!"


# -------------------------------
# PIPELINE EXECUTION
# -------------------------------

def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    df = basic_clean(df)
    df = handle_missing(df)
    df = add_business_features(df)

    validate_data(df)

    return df


# -------------------------------
# SAVE OUTPUT
# -------------------------------

def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# -------------------------------
# CLI
# -------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ETL pipeline")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    df = build_clean_dataset(args.input)
    save_processed(df, args.output)

    print("✅ ETL Pipeline Completed")
    print(f"📁 Output: {args.output}")
    print(f"📊 Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()
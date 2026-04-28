<div align="center">

# 🎧 SpotifyPulse
### Music Analytics & User Insights Platform

*Turning raw listener data into decisions that drive retention, engagement, and growth.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com)

</div>

---

## 🚀 Tagline

> **"From 50,000 listeners to one clear strategy — SpotifyPulse decodes user behavior to predict churn, maximize engagement, and power smarter music experiences."**

---

## 📌 Overview

SpotifyPulse is an end-to-end data analytics platform built on a realistic dataset of **50,000 Spotify users**. It transforms raw behavioral signals — listening hours, skips, playlist activity, subscription type — into actionable intelligence for product, marketing, and recommendation teams.

The platform covers the full analytics lifecycle: data extraction, cleaning, exploratory analysis, statistical hypothesis testing, and KPI reporting. Every insight is grounded in statistical rigor and framed around real business decisions — from reducing churn to optimizing ad conversion and improving recommendation quality.

---

## 🧩 Problem Statement

Music streaming is a retention game. Spotify competes not just on catalog size, but on how well it keeps users engaged. The core challenge:

- **Who is about to churn** — and why?
- **What behavioral patterns** separate highly engaged users from passive ones?
- **Which subscription tiers and genres** drive the most platform value?
- **How do audio preferences and usage habits** influence long-term loyalty?

Without data-driven answers, product decisions become guesswork. SpotifyPulse provides the analytical foundation to answer these questions with confidence — enabling proactive retention, smarter recommendations, and higher conversion from free to premium.

---

## 📊 Dataset Overview

| Attribute | Details |
|---|---|
| Source | Realistic synthetic Spotify user behavior dataset |
| Total Records | 50,000 users |
| Features | 18 original + 2 engineered = **20 columns** |
| Coverage | Demographics, subscription, engagement, preferences, churn signals |

**Key Features:**

| Category | Columns |
|---|---|
| Demographics | `user_id`, `country`, `age`, `signup_date` |
| Subscription | `subscription_type`, `subscription_status` |
| Churn Signals | `months_inactive`, `inactive_3_months_flag` |
| Engagement | `avg_listening_hours_per_week`, `playlists_created`, `avg_skips_per_day` |
| Preferences | `favorite_genre`, `most_liked_feature`, `desired_future_feature` |
| Monetization | `ad_interaction`, `ad_conversion_to_subscription` |
| Engineered | `age_group`, `engagement_level` (Low / Medium / High) |

**Data Challenges Addressed:**
- Missing values in `age` (imputed with mean) and `country` (flagged as `unknown`)
- Outlier removal using the IQR method on age
- Inconsistent text casing across categorical fields — standardized to lowercase
- `signup_date` parsed from raw string to proper datetime format

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Pandas & NumPy** | Data wrangling and feature engineering |
| **Matplotlib & Seaborn** | Visualization and charting |
| **SciPy & Statsmodels** | Statistical testing and regression |
| **Jupyter Notebook** | Interactive analysis environment |
| **Google Colab** | Cloud execution and collaboration |

---

## 🏗️ Project Architecture

```
Raw CSV Data
     │
     ▼
┌─────────────────────┐
│  01 · Extraction    │  Load raw data, validate shape & schema
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  02 · Cleaning      │  Dedup, impute, standardize, engineer features
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  03 · EDA           │  Distributions, churn patterns, genre & device trends
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  04 · Statistics    │  Correlation, regression, t-test, ANOVA
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  05 · KPI Load Prep │  13 business KPIs exported for dashboarding
└─────────────────────┘
```

### Notebook Breakdown

| Notebook | Purpose |
|---|---|
| `01_extraction.ipynb` | Load raw CSV, inspect schema, validate data types and shape |
| `02_cleaning.ipynb` | Handle nulls, remove duplicates, fix formats, engineer `age_group` and `engagement_level` |
| `03_eda.ipynb` | Visual exploration of churn, engagement, genre, device, and subscription patterns |
| `04_statistical_analysis.ipynb` | Correlation heatmap, OLS regression, t-test (Free vs Premium), ANOVA (genre) |
| `05_final_load_prep.ipynb` | Compute 13 KPIs and prepare final dataset for dashboard consumption |

---

## 📸 Visual Showcase

> Screenshots from the analysis notebooks

**Churn Distribution & Engagement Breakdown**

![Churn Distribution](assets/churn_distribution.png)

**Numerical Feature Distributions**

![Feature Distributions](assets/feature_distributions.png)

**Correlation Heatmap**

![Correlation Heatmap](assets/correlation_heatmap.png)

**Regression: Playlists Created vs Listening Hours**

![Regression Plot](assets/regression_plot.png)

**Churn Rate by Genre & Engagement Level**

![Genre Churn](assets/genre_churn_rate.png)

> 📁 *Place your exported chart images in an `/assets` folder and update paths above.*

---

## 📈 Key Insights

**1. Engagement is the strongest churn predictor**
Users with low engagement scores (bottom quantile) churn at significantly higher rates. Listening hours, playlist creation, and skip frequency together form a reliable early-warning signal.

**2. Premium users listen more — but not always stay longer**
While premium subscribers average higher weekly listening hours than free users (confirmed via t-test, p < 0.05), inactivity patterns reveal that even premium users churn when recommendation quality drops.

**3. Genre preference shapes platform loyalty**
ANOVA results show statistically significant differences in listening hours across genres. Certain genres consistently correlate with higher engagement and lower churn — a direct input for playlist curation strategy.

**4. Ad conversion is a high-leverage growth lever**
Users who interacted with ads and converted to paid subscriptions show above-average engagement scores, suggesting that targeted ad experiences can drive both acquisition and long-term retention.

**5. The skip rate is an underused churn signal**
High average skips per day strongly correlate with lower listening hours and higher inactivity — making it a real-time proxy for recommendation dissatisfaction before a user formally churns.

**6. Young adults dominate engagement, but mid-age users retain better**
Age group segmentation reveals that while teenagers and young adults drive volume, mid-age users (35–50) show more stable, long-term engagement patterns.

---

## 🧪 Statistical Analysis

| Method | What It Answers |
|---|---|
| **Pearson Correlation** | Which behavioral features move together? (e.g., playlists ↔ listening hours) |
| **OLS Linear Regression** | What predicts weekly listening hours? (age, ratings, playlists, skips as features) |
| **Independent T-Test** | Do Free and Premium users listen significantly differently? |
| **One-Way ANOVA** | Does favorite genre significantly affect listening behavior? |
| **IQR Outlier Detection** | Are extreme age values distorting demographic analysis? |
| **KDE Distribution Analysis** | How is listening time distributed — normal, skewed, or bimodal? |

All tests were conducted at **α = 0.05** significance level. Results are interpreted in both statistical and business terms throughout the notebooks.

---

## 💡 Business Recommendations

**1. Build a churn early-warning system**
Deploy the engagement score (listening hours × 0.4 + playlists × 0.3 − skips × 0.3) as a real-time health metric. Flag users dropping below the low-engagement threshold for proactive outreach.

**2. Personalize re-engagement campaigns by genre**
Since genre preference significantly impacts listening behavior, tailor win-back campaigns with genre-specific content drops, exclusive releases, or curated playlists aligned to each user's taste profile.

**3. Optimize the free-to-premium conversion funnel**
Ad-converted users show strong post-conversion engagement. Invest in smarter ad targeting for free users showing medium-to-high engagement scores — they're the most conversion-ready segment.

**4. Reduce skip rates through better recommendations**
High skip rates are a leading indicator of churn. Improving recommendation relevance — especially in the first 5 songs of any session — can directly reduce skip frequency and improve retention.

**5. Design subscription tiers around behavioral segments**
The data supports distinct behavioral clusters (low, medium, high engagement). Tailor pricing, features, and perks to each segment rather than applying a one-size-fits-all premium strategy.

---

## 🎯 Impact

| Stakeholder | Value Delivered |
|---|---|
| **Product Teams** | Behavioral KPIs and engagement scoring to prioritize feature development |
| **Marketing Teams** | Segment-level churn risk scores for targeted retention campaigns |
| **Data Science Teams** | Clean, feature-engineered dataset ready for ML model training |
| **Business Leadership** | 13 executive KPIs covering churn, engagement, conversion, and activity |

SpotifyPulse demonstrates how structured behavioral analytics can reduce churn, increase premium conversion, and improve recommendation quality — directly impacting Monthly Active Users (MAU) and Average Revenue Per User (ARPU).

---

## 📂 Folder Structure

```
E_G17_SpotifyPulse/
│
├── 📁 data/
│   ├── raw/
│   │   └── spotify_user_behavior_realistic_50000_rows.csv
│   └── cleaned/
│       └── spotify_cleaned.csv
│
├── 📁 notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
│
├── 📁 docs/
│   └── data_dictionary.md
│
├── 📁 assets/              ← chart exports & screenshots
│
└── README.md
```

---

## 🧑‍💻 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Dadi-Dinesh/E_G17_SpotifyPulse.git
cd E_G17_SpotifyPulse
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels jupyter
```

**3. Launch Jupyter**
```bash
jupyter notebook
```

**4. Run notebooks in order**
```
01_extraction.ipynb       → Load and inspect raw data
02_cleaning.ipynb         → Clean, transform, engineer features
03_eda.ipynb              → Explore patterns and visualize trends
04_statistical_analysis.ipynb  → Run statistical tests
05_final_load_prep.ipynb  → Generate KPIs and final dataset
```

> 💡 Notebooks are also compatible with **Google Colab** — open any `.ipynb` directly via the Colab badge inside each notebook.

---

## 🔮 Future Scope

- **ML-Powered Churn Prediction** — Train classification models (XGBoost, Random Forest) on the engineered features to predict churn probability per user
- **Real-Time Analytics Pipeline** — Integrate with Spotify's API or a streaming source (Kafka) for live behavioral monitoring
- **User Segmentation with Clustering** — Apply K-Means or DBSCAN to discover natural user personas beyond the manual engagement tiers
- **Recommendation Quality Scoring** — Build a feedback loop between skip rates and recommendation engine outputs to measure and improve relevance
- **Interactive Dashboard** — Deploy a Streamlit or Tableau dashboard for non-technical stakeholders to explore KPIs dynamically

---

## 🤝 Contributors

| Name | Role |
|---|---|
| Agrima Ojha | KPI Preparation & Dashboard Load |
| Himani Pinjani | Data Cleaning & Preprocessing |
| Dadi Dinesh | Data Engineering & Pipeline Architecture |
| Anurag Pandey | Exploratory Data Analysis & Visualizations |
| Vedant Satbhai | Statistical Analysis & Report |
---

<div align="center">

---

*"Turning data into decisions."*

⭐ If this project helped you, consider giving it a star!

</div>

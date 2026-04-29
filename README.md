# 🎧 SpotifyPulse — User Retention & Engagement Intelligence  
**NST DVA Capstone 2 | Newton School of Technology**  
**Team G-17**

---

## 🚀 Project Overview

SpotifyPulse is a data analytics project focused on analyzing **user churn, engagement behavior, and retention patterns** in a music streaming platform.

The project converts raw user activity data into **actionable business insights** using Python, ETL pipelines, and Tableau dashboards.

---

Tableau Link- https://public.tableau.com/views/SpotifyPulse/UserRetentionDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---
## 🎯 Business Problem

Music streaming platforms face high competition and user churn.  
Stakeholders need to:

- Identify users likely to churn  
- Understand behavioral patterns affecting engagement  
- Improve retention through data-driven strategies  

---

## ❓ Core Business Question

**What user behaviors and engagement patterns drive churn, and how can they be used to improve retention?**

---

## 💡 Decision Supported

- Identify high-risk users early  
- Optimize engagement strategies  
- Improve subscription retention  
- Enable targeted interventions  

---

## 📊 Dataset

| Attribute | Details |
|----------|--------|
| Source | Kaggle (Spotify dataset) |
| Format | CSV |
| Rows | 50,000+ |
| Columns | 15+ |
| Key Features | Engagement Score, Skips, Listening Hours, Subscription Type |

---

## 🔑 Key Columns Used

| Column | Description | Role |
|-------|------------|------|
| Engagement Score | User activity level | KPI |
| Avg Skips Per Day | Skip behavior | Churn predictor |
| Listening Hours | Time spent listening | Engagement metric |
| Inactive 3 Months Flag | Churn indicator | Target |
| Subscription Type | Plan type | Segmentation |
| Risk Level | Derived churn risk | Decision |

---

## 📈 KPI Framework

| KPI | Definition | Formula |
|-----|----------|--------|
| Churn Rate | % users inactive for 3+ months | churned / total |
| At Risk Users | Users likely to churn | behavioral threshold |
| Active Users | Engaged users | active / total |
| Avg Inactivity | Avg months inactive | mean(months_inactive) |

---

## 📊 Tableau Dashboards

### 1️⃣ User Retention Dashboard
- Churn rate and user segmentation  
- Risk-level distribution  
- Engagement vs churn patterns  
- Skip behavior impact on churn  

---

### 2️⃣ Engagement Analysis Dashboard
- Listening time vs engagement  
- Engagement score distribution  
- Device and genre analysis  
- Age group engagement trends  

---

### 3️⃣ User Behavior & Risk Intelligence Dashboard
- Churn heatmap (Engagement vs Skips)  
- Subscription impact on churn  
- Country-level churn patterns  
- Feature usage insights  

---

## 🔍 Key Insights

1. Higher skip behavior strongly correlates with higher churn  
2. Users with low engagement scores are most likely to churn  
3. Increased listening hours improves retention  
4. Premium users show lower churn than free users  
5. Certain countries exhibit higher churn rates  
6. Engagement drops significantly before churn  
7. High inactivity directly leads to churn  
8. Subscription type influences engagement behavior  

---

## 💡 Recommendations

| Insight | Recommendation | Expected Impact |
|--------|--------------|----------------|
| High skip behavior | Improve recommendation system | Reduce churn |
| Low engagement users | Targeted notifications | Increase retention |
| Free users churn more | Convert to premium plans | Higher revenue |
| Low listening hours | Personalized playlists | Boost engagement |

---

## 🛠 Tech Stack

- Python (Pandas, NumPy)
- Jupyter Notebook
- Tableau Public
- GitHub

---

## 📁 Repository Structure
SpotifyPulse/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_extraction.ipynb
│ ├── 02_cleaning.ipynb
│ ├── 03_eda.ipynb
│ ├── 04_statistical_analysis.ipynb
│ └── 05_final_load_prep.ipynb
│
├── scripts/
│ └── etl_pipeline.py
│
├── tableau/
│ ├── screenshots/
│ └── dashboard_links.md
│
├── reports/
├── docs/
│ └── data_dictionary.md
│
└── README.md


---

## 👥 Team G-17

| Name | Role |
|------|-----|
| Agrima Ojha | Project Lead, ETL, Dashboard |
| Himani Pinjani | EDA & Analysis |
| Anurag Pandey | Statistical Analysis |
| Dadidinesh | Dataset & ETL, Report |
| Ritesh Kumar | Statistical Analysis |
| Vedant Satbhai | Statistical Analysis, ReadME |

---

## 📌 Conclusion

SpotifyPulse provides a comprehensive understanding of **user churn and engagement dynamics**, enabling businesses to take **data-driven decisions to improve retention and user experience**.

---

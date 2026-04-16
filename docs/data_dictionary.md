# 🎧 Spotify User Behavior Dataset – Data Dictionary

This document describes the structure, variables, and meaning of each column in the Spotify User Behavior dataset. The dataset captures user demographics, engagement patterns, subscription details, and listening behavior.

---

## 📁 Dataset Overview

* **Total Records:** ~50,000 users
* **Focus:** User engagement, subscription behavior, and churn indicators

---

## 🧾 Column Descriptions

| Column Name   | Data Type | Description                             |
| ------------- | --------- | --------------------------------------- |
| `user_id`     | Integer   | Unique identifier for each user         |
| `country`     | String    | Country of the user                     |
| `age`         | Integer   | Age of the user                         |
| `signup_date` | Date      | Date when the user signed up on Spotify |

---

## 💳 Subscription Details

| Column Name           | Data Type | Description                           |
| --------------------- | --------- | ------------------------------------- |
| `subscription_type`   | String    | Type of subscription (Free / Premium) |
| `subscription_status` | String    | Current status (Active / Cancelled)   |

---

## ⚠️ Churn Indicators

| Column Name              | Data Type    | Description                                                |
| ------------------------ | ------------ | ---------------------------------------------------------- |
| `months_inactive`        | Integer      | Number of months the user has been inactive                |
| `inactive_3_months_flag` | Binary (0/1) | Indicates if user inactive for ≥3 months (1 = Yes, 0 = No) |

---

## 📢 Ads & Conversion

| Column Name                     | Data Type    | Description                                           |
| ------------------------------- | ------------ | ----------------------------------------------------- |
| `ad_interaction`                | Binary (0/1) | Whether user interacted with ads                      |
| `ad_conversion_to_subscription` | Binary (0/1) | Whether user converted to paid subscription after ads |

---

## 🎵 User Experience & Preferences

| Column Name                      | Data Type | Description                                                       |
| -------------------------------- | --------- | ----------------------------------------------------------------- |
| `music_suggestion_rating_1_to_5` | Integer   | User rating for Spotify recommendations (1 = Poor, 5 = Excellent) |
| `favorite_genre`                 | String    | User’s preferred music genre                                      |
| `most_liked_feature`             | String    | Feature user likes most (e.g., playlists, recommendations)        |
| `desired_future_feature`         | String    | Feature user wants in the future                                  |

---

## 📱 Usage Behavior

| Column Name                    | Data Type | Description                                        |
| ------------------------------ | --------- | -------------------------------------------------- |
| `avg_listening_hours_per_week` | Float     | Average hours spent listening per week             |
| `primary_device`               | String    | Device mostly used (Mobile, Desktop, Tablet, etc.) |
| `playlists_created`            | Integer   | Number of playlists created by user                |
| `avg_skips_per_day`            | Integer   | Average number of songs skipped per day            |

---

## 📌 Notes

* Binary columns use **1 = Yes, 0 = No**
* Higher inactivity and skips may indicate **potential churn**
* Engagement metrics help analyze **user retention and satisfaction**

---

## 🎯 Use Cases

* Predict user churn 📉
* Improve recommendation systems 🎯
* Analyze user engagement patterns 📊
* Optimize subscription conversion strategies 💡

---

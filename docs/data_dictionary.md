# 🎧 Spotify User Behavior Dataset – Data Dictionary

This document describes the structure, variables, and meaning of each column in the Spotify User Behavior dataset. The dataset captures user demographics, engagement patterns, subscription details, and listening behavior.

---

## 📁 Dataset Overview

**This dataset consists of approximately 50,000 users, offering a comprehensive view of user activity and platform interaction. It is designed to support analysis in key areas such as user engagement, subscription behavior, and churn prediction.
* **Focus:** By capturing patterns in how users interact with the platform, the dataset enables deeper insights into retention trends, customer lifecycle stages, and factors influencing user decisions. It serves as a strong foundation for building data-driven models and strategies aimed at improving user experience and reducing churn.

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

* Binary columns are encoded as 1 = Yes and 0 = No for simplicity and consistency in analysis.**
* Increased inactivity levels and frequent skips can serve as early indicators of potential churn.**
* Engagement-related metrics play a crucial role in understanding user retention, behavior patterns, and overall satisfaction**

---

## 🎯 Use Cases

* Churn prediction :Identify at-risk users early using inactivity flags, skip rates, and subscription status to trigger timely retention actions.
* Recommendation enhancement : Leverage genre preferences, ratings, and most-liked features to personalize and improve content delivery.
* Engagement analysis :Track listening hours, playlists, and skip behavior over time to uncover platform interaction patterns.
* Subscription conversion : Analyze ad interaction and conversion rates to optimize upgrade funnels and drive revenue growth.


---

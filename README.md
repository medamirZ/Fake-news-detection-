# 📰 Fake News Detection — End-to-End Pipeline (LIAR Dataset)

A complete end-to-end data pipeline for Fake News Detection using the LIAR dataset.  
This project includes data exploration, preprocessing, feature engineering, speaker-history analysis, and machine-learning modeling.

---

## 📌 Project Overview

This repository contains a full workflow for detecting fake news using a combination of:

- **Statement text**
- **Speaker credibility features** (truth history counts)
- **Metadata** (subject, party affiliation, state info, context)

The project is organized into **four collaborative branches**, each representing a stage of the pipeline:

1. **data-exploration** → Exploratory Data Analysis (EDA)
2. **data-cleaning** → Missing values, duplicates, preprocessing
3. **data-transformation** → Feature engineering and encoding
4. **modeling** → Machine-learning models and evaluation

The `main` branch holds the final, stable code.

---

## 📊 Dataset Description

The dataset contains:

- **9 object columns**
- **5 float columns** (speaker-history truth counts)

Key columns include:

- `Label` — truth category (LIAR dataset classes)
- `Statement` — text of the claim
- `Speaker` — who made the statement
- `Party Affiliation` — political party (important predictive feature)
- `Barely True Counts`, `False Counts`, ... — **speaker credibility history**
- `Context`, `Subject`, `State Info`


## 🛠 Workflow & Branching Strategy (For Team Members)

This project uses a **feature-branch workflow**.  
Each team member works only on **one dedicated branch**.

### Branch Responsibilities

| Branch | Owner | Work |
|--------|--------|------|
| `data-exploration` | You | EDA, summaries, profiling |
| `data-cleaning` | Member 1 | Handling NaN, duplicates, preprocessing |
| `data-transformation` | Member 2 | Encoding, feature engineering |
| `modeling` | Member 3 | ML models, evaluation |

### ✔ Main Rules
- Each member can push **only** to their assigned branch  


git clone https://github.com/medamirZ/Fake-news-detection-.git
cd Fake-news-detection-

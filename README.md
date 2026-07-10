# Human Development Index (HDI) Predictor

A machine learning web application that predicts a country's Human Development Index (HDI) score based on four key development indicators — life expectancy, expected years of schooling, mean years of schooling, and gross national income per capita.

## Overview

The Human Development Index is a composite statistic used by the UNDP to rank countries into four tiers of human development (Low, Medium, High, Very High), based on life expectancy, education, and income per capita. This project builds a Linear Regression model trained on UNDP data for 195 countries, and deploys it through a Flask web application where users can input the four indicators and instantly receive a predicted HDI score and development category.

## Tech Stack

- **Python 3.13**
- **Flask** — web framework and routing
- **scikit-learn** — Linear Regression model
- **Pandas / NumPy** — data loading, cleaning, and preprocessing
- **Pickle** — model serialization
- **HTML/CSS** — frontend templates

## Project Structure

well_being_project/
│
├── app.py                     # Flask application (routes + model loading)
├── Dataset/
│   └── HDI.csv                 # UNDP Human Development Index dataset
├── models/
│   └── HDI.pkl                 # Trained and serialized Linear Regression model
├── Training/
│   └── HumDevIndex.ipynb       # Notebook: data cleaning, training, evaluation
├── templates/
│   ├── index.html               # Input form (landing page)
│   └── dashboard.html           # Prediction result page
├── static/
└── README.md

## Dataset

Source: UNDP Human Development Reports (via Kaggle) — 195 countries, historical indicators from 1990–2021. Five 2021 columns were used for this model (target: HDI, features: life expectancy, expected/mean schooling, GNI per capita). Rows with missing values in these columns were dropped during preprocessing.

## Machine Learning Workflow

1. **Data Loading** — Imported the HDI dataset using Pandas.
2. **Feature Selection** — life expectancy, expected/mean schooling, GNI per capita as X; HDI as y.
3. **Data Cleaning** — Checked nulls with `isnull().sum()`, dropped incomplete rows.
4. **Train/Test Split** — 80/20 split (`random_state=42`).
5. **Model Training** — Fit a `LinearRegression` model.
6. **Evaluation** — R² = 0.98, MSE ≈ 0.0005 on the test set.
7. **Model Serialization** — Saved as `models/HDI.pkl` via Pickle.

## Web Application

- **`/`** — Landing page, input form.
- **`/dashboard`** (POST) — Predicts and renders result with an animated score gauge.

### HDI Categories

| Score Range | Category |
|---|---|
| ≥ 0.80 | Very High |
| 0.70 – 0.79 | High |
| 0.55 – 0.69 | Medium |
| < 0.55 | Low |

## Running Locally

```bash
git clone <your-repo-url>
cd well_being_project
pip install flask pandas numpy scikit-learn matplotlib jupyter
python app.py
# open http://127.0.0.1:5000
```

## Sample Prediction

| Input | Value |
|---|---|
| Life Expectancy | 73.5 years |
| Expected Schooling | 13.4 years |
| Mean Schooling | 8.0 years |
| GNI per Capita | $15,000 |

**Predicted HDI: 0.711 → High Human Development**

## Author

Aarrnave — B.Tech CSE, SRKR Engineering College
Project developed as part of the Skill Wallet Virtual Internship Program.
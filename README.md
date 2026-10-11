# House Price Prediction Using Machine Learning

## 📌 Project Overview

This project focuses on predicting house prices using Machine Learning algorithms and the Bengaluru House Price dataset.

The project follows an end-to-end Machine Learning workflow, including data exploration, data cleaning, feature engineering, preprocessing, model training, model evaluation, and hyperparameter tuning.

The main objective is to compare multiple regression algorithms and identify a suitable model for house price prediction.

## 🎯 Objectives

- Explore and understand the dataset using Exploratory Data Analysis (EDA).
- Handle missing values and duplicate records.
- Clean and prepare the dataset.
- Perform feature engineering.
- Encode categorical features and scale numerical features.
- Train multiple Machine Learning regression models.
- Evaluate models using MAE, RMSE, and R².
- Compare baseline models and perform hyperparameter tuning.
- Save the model and preprocessing pipeline for future predictions.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Joblib
- Git and GitHub

## Dataset

The project uses the Bengaluru House Price dataset.

**Target variable:** `price`

**Input features used for modelling:**

- `area_type`
- `location`
- `total_sqft`
- `bath`
- `balcony`
- `BHK`
- `sqft_per_bhk`

The `price_per_sqft` feature is excluded from model inputs because it is calculated using the target price and could cause target leakage.

## 🤖 Machine Learning Algorithms

The following regression algorithms were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. XGBoost Regressor

## 🔄 Project Workflow

1. Dataset collection and understanding
2. Exploratory Data Analysis (EDA)
3. Data cleaning
4. Feature engineering
5. Train-test split
6. Data preprocessing
7. Model training
8. Model evaluation and comparison
9. Hyperparameter tuning
10. Model saving
11. House price prediction

## 📊 Model Evaluation

The baseline models were evaluated using the same train-test split and the following metrics.

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 45.2360 | 125.3719 | 0.4592 |
| Decision Tree | 40.3996 | 120.8564 | 0.4975 |
| Random Forest | 33.3099 | 100.3635 | 0.6534 |
| Gradient Boosting | 39.1581 | 101.4037 | 0.6462 |
| XGBoost | 35.1745 | 94.4562 | 0.6930 |

### Baseline Model Comparison

- **Best R²:** XGBoost — 0.6930
- **Lowest RMSE:** XGBoost — 94.4562
- **Lowest MAE:** Random Forest — 33.3099

Based on the current baseline results, XGBoost is the leading candidate overall, while Random Forest has the lowest MAE.

*Note: Metric values are in the dataset's target-price units. The results represent the current experiment and should be revalidated before deployment.*

## Hyperparameter Tuning

GridSearchCV was used to tune the XGBoost model.

Best parameters from the current search:

- `learning_rate`: 0.1
- `max_depth`: 3
- `n_estimators`: 200
- `subsample`: 1.0

The tuned model achieved the following test results:

| Metric | Tuned XGBoost |
|---|---:|
| MAE | 38.7673 |
| RMSE | 101.7191 |
| R² | 0.6440 |

The tuned model did not outperform the baseline XGBoost model in this experiment. Therefore, the baseline remains the better candidate based on the current test results.

## Project Structure

```text
House-Price-Analysis-Using-ML-Model/
│
├── data/
├── notebook/
├── model/
├── output/
├── src/
├── LICENSE
└── README.md
```

## 📊Evaluation Metrics

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted prices. Lower is better.
- **RMSE (Root Mean Squared Error):** Penalizes larger prediction errors. Lower is better.
- **R² Score:** Measures how well the model explains the variation in the target. Higher is generally better.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/HarishMayakuntla/House-Price-Analysis-Using-ML-Model.git
```

### 2. Open the project folder

```bash
cd House-Price-Analysis-Using-ML-Model
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib scikit-learn xgboost joblib jupyter
```

### 4. Explore the notebooks

Open Jupyter Notebook and run the notebooks in the appropriate workflow order.

```bash
jupyter notebook
```

*Note: Run the prediction script only after the trained model and matching fitted preprocessor have been saved to the expected paths.*

## 📈 Future Improvements

- Further improve model performance through feature selection and tuning.
- Validate predictions on unseen data.
- Build a user-friendly prediction interface.
- Deploy the model using FastAPI or Streamlit.
- Add visualizations and prediction examples.

## 👨‍💻 Author

**Harish Mayakuntla**

Aspiring Data Scientist | Machine Learning | Python | SQL

GitHub: [HarishMayakuntla](https://github.com/HarishMayakuntla)

## 🚧 Project Status

**Currently under development.**

New features, experiments, results, and documentation will be added progressively throughout the project.

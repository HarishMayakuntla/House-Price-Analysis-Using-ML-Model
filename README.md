# 🏠 Bengaluru House Price Prediction Using Machine Learning

An end-to-end Machine Learning project that predicts estimated residential property prices in Bengaluru based on property features. The project includes data analysis, preprocessing, feature engineering, model training, evaluation, and a deployed Streamlit web application.

<p align="center">

  **🚀 Live Demo:** [Try the House Price Prediction App](https://house-price-prediction-harish.streamlit.app/)

  **💻 GitHub Repository:** [House-Price-Analysis-Using-ML-Model](https://github.com/HarishMayakuntla/House-Price-Analysis-Using-ML-Model)

</p>

---

## 📌 Project Overview

House prices depend on several factors, including location, property size, number of bedrooms, bathrooms, and property type.

This project uses Machine Learning regression algorithms to learn patterns from Bengaluru housing data and estimate property prices from user-provided details.

The trained model and preprocessing pipeline are integrated into a Streamlit application, allowing users to make predictions through an interactive web interface.

## ✨ Key Features

- Predict estimated Bengaluru residential property prices.
- Interactive web interface built with Streamlit.
- Accepts location, area type, square footage, BHK, bathrooms, and balconies.
- Performs feature engineering and data preprocessing.
- Experiments with multiple regression algorithms.
- Evaluates models using standard regression metrics.
- Saves and loads the trained model and preprocessing pipeline.
- Deployed web application accessible through a public URL.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Matplotlib & Seaborn | Exploratory data visualization |
| Scikit-learn | Preprocessing, regression, and evaluation |
| XGBoost | Gradient-boosted regression |
| Joblib | Saving and loading model artifacts |
| Streamlit | Interactive web application |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Web application deployment |

## 📂 Dataset and Features

The project uses Bengaluru house price data.

The main features used by the application include:

| Feature | Description |
|---|---|
| `area_type` | Type of property area |
| `location` | Property location |
| `total_sqft` | Total area in square feet |
| `bath` | Number of bathrooms |
| `balcony` | Number of balconies |
| `BHK` | Number of bedrooms, hall, and kitchen |
| `sqft_per_bhk` | Total square feet divided by BHK |

**Target variable:** `price`

The target price is used during training. At prediction time, the model receives property details and estimates the price.

## 🔄 Machine Learning Workflow

1. **Data Understanding:** Inspect dataset structure, columns, and data types.
2. **Exploratory Data Analysis:** Examine distributions, missing values, relationships, and outliers.
3. **Data Cleaning:** Handle missing values and prepare data for modeling.
4. **Feature Engineering:** Create useful features such as `sqft_per_bhk`.
5. **Preprocessing:** Impute missing values, scale numerical features, and encode categorical features.
6. **Model Training:** Train and compare regression algorithms.
7. **Model Evaluation:** Evaluate predictions using MAE, RMSE, and R².
8. **Hyperparameter Tuning:** Search for improved model configurations.
9. **Model Serialization:** Save the trained model and preprocessing pipeline using Joblib.
10. **Deployment:** Build and deploy the Streamlit prediction application.

## 🤖 Models Explored

The project explores regression algorithms including:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### Evaluation Metrics

- **MAE — Mean Absolute Error:** Average absolute difference between actual and predicted prices.
- **RMSE — Root Mean Squared Error:** Measures prediction error while penalizing larger errors more heavily.
- **R² Score:** Measures how much variation in the target is explained by the model.

The best model should be selected based on evaluation results on held-out data, not training performance alone.

## 🌐 Live Application

Try the deployed application:

👉 **[Open House Price Prediction](https://house-price-prediction-harish.streamlit.app/)**

### How to Use

1. Open the live application.
2. Select the property area type.
3. Enter the property location.
4. Enter the total square footage.
5. Specify the number of bathrooms, balconies, and BHK.
6. Click **Predict House Price**.
7. View the estimated property value.

## 📁 Repository Structure

```text
House-Price-Analysis-Using-ML-Model/
│
├── data/
│   └── Dataset and data documentation
│
├── model/
│   ├── House_price_prediction_model.pkl
│   └── House_price_preprocessor.pkl
│
├── notebook/
│   └── Jupyter notebooks for analysis and modeling
│
├── output/
│   └── Analysis plots and model results
│
├── src/
│   └── Data cleaning, feature engineering,
│       preprocessing, and prediction code
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

*The structure above describes the intended project layout. Confirm the actual filenames in the repository before relying on the file list.*

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/HarishMayakuntla/House-Price-Analysis-Using-ML-Model.git
```

### 2. Navigate to the project folder

```bash
cd House-Price-Analysis-Using-ML-Model
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

**Note:** Keep the trained model and preprocessing files in the `model/` directory, using the exact filenames referenced in `app.py`.

## ⚠️ Limitations

- Predictions are estimates and may differ from actual market prices.
- Accuracy depends on the quality, coverage, and relevance of the training data.
- Unseen locations may receive predictions even when the model has not learned location-specific patterns for them.
- Property prices change over time, so retraining with more recent data may be necessary.

This application is intended for educational and informational purposes, not as an official property valuation tool.

## 👨‍💻 Author

**Harish Mayakuntla**

Aspiring Data Scientist | Machine Learning | Python | SQL

- **GitHub:** [HarishMayakuntla](https://github.com/HarishMayakuntla)
- **LinkedIn:** [Harish Mayakuntla](https://www.linkedin.com/in/harish-mayakuntla/)

## 🎯 Project Objective

To develop practical end-to-end Machine Learning skills by building a complete regression project, evaluating different algorithms, and deploying a model as an interactive web application.

---

⭐ If you find this project interesting, explore the repository and try the live demo.

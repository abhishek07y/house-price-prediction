# 🏠 Bangalore House Price Prediction

A Machine Learning project that predicts house prices in Bangalore based on various property-related features.

## 📌 Project Overview

This project uses Machine Learning to predict the price of houses in Bangalore.

The complete workflow includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Handling Missing Values
- Outlier Detection and Removal
- Feature Engineering
- Data Preprocessing
- Model Building
- Model Evaluation
- Hyperparameter Tuning
- Model Deployment

## 🎯 Objective

The main objective of this project is to build a reliable regression model that can predict Bangalore house prices based on features such as location, number of bedrooms, total area, bathrooms, etc.

## 📊 Dataset

The dataset contains information about Bangalore residential properties.

Important features include:

- `location`
- `total_sqft`
- `bath`
- `balcony`
- `size`
- `price`

Target variable:

- `price`

## 🔎 Exploratory Data Analysis

The following EDA techniques were performed:

- Distribution analysis
- Univariate analysis
- Bivariate analysis
- Correlation analysis
- Categorical feature analysis
- Price distribution analysis
- Location-wise price analysis

## 🧹 Data Preprocessing

The dataset was cleaned before training the model.

Steps included:

- Handling missing values
- Removing duplicate/unnecessary data
- Converting categorical variables
- Feature engineering
- Removing irrelevant columns
- Handling inconsistent values
- Encoding categorical features
- Scaling numerical features where required

## 📈 Outlier Handling

Outliers were identified and removed using statistical/domain-based techniques.

This helped reduce the effect of extreme observations and improved the model's generalization performance.

## ⚙️ Machine Learning Model

### Ridge Regression

Ridge Regression was selected as the final model.

Ridge Regression is a regularized version of Linear Regression that helps reduce overfitting by adding an L2 penalty.

The model was implemented using a Scikit-learn Pipeline along with preprocessing.

## 🔄 ML Pipeline

The project follows this workflow:

Raw Data
↓
Data Cleaning
↓
EDA
↓
Outlier Removal
↓
Feature Engineering
↓
Train-Test Split
↓
Preprocessing
↓
Ridge Regression
↓
Model Evaluation
↓
Prediction

## 📏 Model Evaluation

The model was evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Model Performance

| Metric | Score |
|---|---:|
| Training R² | `YOUR_SCORE` |
| Testing R² | `YOUR_SCORE` |
| MAE | `YOUR_SCORE` |
| RMSE | `YOUR_SCORE` |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Git & GitHub

## 📁 Project Structure

```text
Bangalore-House-Price-Prediction/
│
├── app.py
├── RidgeModel.pkl
├── clean_house.csv
├── requirements.txt
├── README.md
│
└── notebook/
    └── house_price_prediction.ipynb

# 2.Early-Diabetes-Predictor

![App Screenshot](img.jpg)

 Project 2 of my 25 Premium AI Projects Challenge

🩺 Early Diabetes Prediction using Machine Learning
This project is a machine learning application that predicts the likelihood of diabetes based on various medical attributes. It includes end-to-end steps from data preprocessing and exploratory data analysis to model optimization, evaluation, and deployment with a Streamlit app.

🔍 Project Highlights
🧠 Model Used: Support Vector Classifier (SVC)

🔧 Hyperparameter Tuning: Performed using Optuna

📊 Validation: 5-Fold Cross-Validation for performance estimation

📈 EDA & Visualization: Insights extracted using Seaborn and Matplotlib

📐 Feature Engineering: Scaling, handling missing values, and data cleaning

📉 Evaluation: Accuracy, confusion matrix

🌐 Deployment: Deployed as an interactive Streamlit Web App

🧪 Dataset
Source: Pima Indians Diabetes Dataset (from Kaggle/UCI)

Features:

Pregnancies

Glucose

BloodPressure

SkinThickness

Insulin

BMI

DiabetesPedigreeFunction

Age

Target: Binary (0 = Non-diabetic, 1 = Diabetic)


🧪 Model Building & Optimization
Trained an SVC classifier

Used Optuna to optimize C, kernel, gamma, and degree

Used StratifiedKFold cross-validation for reliable scoring

Evaluated with accuracy and confusion matrix

📉 Evaluation
Accuracy score on cross-validation

Confusion Matrix visualized with Seaborn heatmap

Final parameters selected from best Optuna trial

🚀 Streamlit Web App
An easy-to-use interactive web application built using Streamlit:

User inputs the 8 medical features

Model returns whether the person is likely/unlikely to have diabetes

Clean and responsive UI with CSS styling

📁 Folder Structure

📂 early-diabetes-prediction/
├── 📄 README.md
├── 📄 diabeteUI.py                 # Streamlit App
├── 📄 earlyDiabetesPredictor.ipynb  # Model training and Optuna tuning
├── 📄 earlyDiabetesPredictor.pkl
├── 📄 scaler.pkl
└── 📊 diabetes.csv


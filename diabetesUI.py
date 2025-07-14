import streamlit as st
import numpy as np
import joblib

# --- Load model and scaler ---
model = joblib.load("earlyDiabetesPredictor.pkl")
scaler = joblib.load("scaler.pkl")

# --- Page Configuration ---
st.set_page_config(page_title="Early Diabetes Predictor", page_icon="🩺", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        .stButton > button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 0.5em 2em;
            font-weight: bold;
            transition: 0.3s;
        }

        .stButton > button:hover,
        .stButton > button:active,
        .stButton > button:focus {
            background-color: #007bff !important;
            color: white !important;
        }

        .prediction-box {
            margin-top: 1.5rem;
            padding: 1.2rem;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }

        .positive {
            background-color: #ffe5e5;
            color: #cc0000;
            border: 2px solid #cc0000;
        }

        .negative {
            background-color: #e6ffed;
            color: #006600;
            border: 2px solid #009900;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h2 style='text-align: center;'>🩺 Early Diabetes Prediction App</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Enter the medical information below to get a prediction</p>", unsafe_allow_html=True)

# --- Layout in Columns ---
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=1)
        glucose = st.number_input("Glucose", min_value=0.0, max_value=199.0, value=100.0)
        blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=122.0, value=70.0)
        skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=99.0, value=20.0)

    with col2:
        insulin = st.number_input("Insulin", min_value=0.0, max_value=846.0, value=80.0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=25.0, format="%.1f")
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.078, max_value=2.42, value=0.5, format="%.3f")
        age = st.number_input("Age", min_value=21, max_value=81, value=33)

# --- Submit Button ---
predict = st.button("🔍 Predict")

# --- Prediction Section Below Button ---
if predict:
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    # --- Styled Result Box ---
    if prediction[0] == 1:
        st.markdown(
            "<div class='prediction-box positive'>⚠️ The model predicts that this person is <strong>likely to have diabetes</strong>.</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='prediction-box negative'>✅ The model predicts that this person is <strong>unlikely to have diabetes</strong>.</div>",
            unsafe_allow_html=True
        )

# --- Footer ---
st.markdown("""
    <hr style="margin-top: 3rem; margin-bottom: 1rem;">
    <p style="text-align: center; color: gray; font-size: 14px;">
        Made with ❤️ by <strong>Muhammad Zaid Naeem</strong>
    </p>
""", unsafe_allow_html=True)

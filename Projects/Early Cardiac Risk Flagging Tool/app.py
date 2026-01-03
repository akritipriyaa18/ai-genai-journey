import streamlit as st
import pandas as pd
from utils.predictor import predict_urgency

st.title("Early Cardiac Risk Flagging Tool")

#Columns Layout
col1, col2 = st.columns(2)

#Left Side: Input Panel
with col1:
    st.header("Patient Information")

    age = st.number_input("Age", min_value = 0, max_value=120, value=30)
    bp = st.number_input("BP", min_value=80, max_value=200, value=100)
    max_hr = st.number_input("Max HR", min_value=30, max_value=200, value=70)
    cholesterol = st.number_input("Cholesterol", min_value=120, max_value=400, value=120)
    symptoms = st.text_area("Symptoms")

    heart_disease = st.selectbox(
        "History of Heart Disease",
        ["No", "Yes"]
    )

    heart_disease_encoded = 1 if heart_disease == "Yes" else 0 

    analyze_btn = st.button("Analyze Patient")

#Right Side:Assistant Panel
with col2:
    st.header("Assistant Panel")
    
    if analyze_btn:
        st.info("🩺 Analyzing patient condition...")
        patient_data = {
            "Age": age,
            "BP" : bp,
            "Cholesterol": cholesterol,
            "Heart_Disease_encoded": heart_disease_encoded,
            "Max HR": max_hr
        }

        urgency, explanation, action = predict_urgency(patient_data)

        st.subheader(f"⚠️ Urgency Level: {urgency}")
        st.write(f"**Reason:** {explanation}")
        st.write(f"**Suggested Action:** {action}")
    else:
        st.write("Waiting for patient data.....")

    

st.markdown("@Akriti")
st.divider()
import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "cardiac_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURES = ['Age', 'Heart_Disease_encoded', 'BP', 'Max HR', 'Cholesterol']

def predict_urgency(patient_data: dict):
    # Ensure DataFrame columns match pipeline exactly in name and order
    df = pd.DataFrame([patient_data], columns=FEATURES)

    urgency_level = model.predict(df)[0]

    # Map urgency to explanation and action
    if urgency_level == "Low Risk":
        explanation = "Patient shows low cardiac risk indicators."
        action = "Routine monitoring recommended."
    elif urgency_level == "Moderate Risk":
        explanation = "Patient shows moderate cardiac risk indicators."
        action = "Schedule cardiology follow-up."
    else:
        explanation = "Patient shows high cardiac risk indicators."
        action = "Immediate medical attention required."

    return urgency_level, explanation, action

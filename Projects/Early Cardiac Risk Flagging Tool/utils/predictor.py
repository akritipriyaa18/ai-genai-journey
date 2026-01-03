import os
import pickle
import pandas as pd


model_path = os.path.join(os.path.dirname(__file__), "..", "model", "cardiac_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_urgency(patient_data):
    df = pd.DataFrame([patient_data])
    urgency_level = model.predict(df)[0]

    explanation = f"Based on input features, the predicted risk is {urgency_level}."

    if urgency_level == "High":
        action = "Immediate medical attention required"
    elif urgency_level == "Medium":
        action = "Monitor closely and run further tests"
    else:
        action = "Routine care recommended"

    return urgency_level, explanation, action
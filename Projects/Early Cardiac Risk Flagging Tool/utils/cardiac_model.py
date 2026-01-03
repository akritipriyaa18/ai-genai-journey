import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Heart_Disease_Prediction.csv")

df = pd.read_csv(DATA_PATH)

le = LabelEncoder()
df['Heart_Disease_encoded'] = le.fit_transform(df['Heart Disease'])

def risk_category(st_depression):
    if st_depression < 1.0:
        return "Low Risk"
    elif st_depression < 2.0:
        return "Moderate Risk"
    else:
        return "High Risk"

df['Risk'] = df['ST depression'].apply(risk_category)

features = ['Age', 'Heart_Disease_encoded', 'BP', 'Max HR', 'Cholesterol']
x = df[features]
y = df['Risk']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(x_train, y_train)

y_pred = pipeline.predict(x_test)


new_patient = pd.DataFrame({
    "Age": [62],
    "Heart Disease_encoded": [1]
})

MODEL_DIR = os.path.join(BASE_DIR, "model")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "cardiac_model.pkl")

with open(MODEL_PATH, "wb") as f:
    pickle.dump(pipeline, f)

print("Model trained and successully saved")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import pipeline
import pickle

df = pd.read_csv("Heart_Disease_Prediction.csv")

le = LabelEncoder()
df['Heart Disease_encoded'] = le.fit_transform(df['Heart Disease'])

def risk_category(st_depression):
    if st_depression < 1.0:
        return "Low Risk"
    elif st_depression < 2.0:
        return "Moderate Risk"
    else:
        return "High Risk"

df['Risk'] = df['ST depression'].apply(risk_category)

features = ['Age', 'Heart_Disease_encoded', 'BP', 'Heart_Rate', 'Cholesterol']
x = df[features]
y = df['Risk']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

pipeline = pipeline([
    ('scaler', StandardSacler()),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(x_train, y_train)

y_pred = pipeline.predict(x_test)


new_patient = pd.DataFrame({
    "Age": [62],
    "Heart Disease_encoded": [1]
})

with open("../model/cardiac_model.pkl", "wb") as f:
   pickle.dump(pipeline, f)

print("Model trained and successully saved")
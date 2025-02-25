import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("diabetes_prediction_dataset.csv")

X = df.iloc[:, :-1] 
y = df.iloc[:, -1]   

categorical_cols = X.select_dtypes(include=['object']).columns
import numpy as np


encoders = {}
for col in categorical_cols:
    encoders[col] = LabelEncoder()
    X[col] = encoders[col].fit_transform(X[col]) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  

def predict_Diabetes_disease(user_input):
    user_df = pd.DataFrame([user_input])

    user_df = user_df[[col for col in user_df.columns if col in X.columns]]

    for col in X.columns:
        if col not in user_df:
            user_df[col] = X[col].median()

    for col in categorical_cols:
        if col in user_df:
            user_df[col] = encoders[col].transform(user_df[col])

    user_df = user_df[X.columns]
    prediction = model.predict(user_df)[0]
    if prediction in label_encoder.classes_:
        prediction_label = label_encoder.inverse_transform([prediction])[0]
    else:
        prediction_label = "Unknown (New Label Detected)"

    probability = model.predict_proba(user_df)[0][1]
    result=''
    print("\n🔎 **Diabetes Disease Prediction:**", "⚠️ At Risk" if prediction else "✅ Not at Risk")
    if prediction:
        result="⚠️ At Risk"
    else:
        result="✅ Not at Risk"
    print(f"📊 **Risk Probability:** {probability * 100:.2f}%")
    
    return result, probability


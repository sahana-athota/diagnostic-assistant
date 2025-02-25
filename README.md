# Diagnostic Assistant - AI-Powered Disease Prediction

## Overview
**Diagnostic Assistant** is an AI-driven web application that enables users to self-diagnose potential diseases based on their symptoms. By leveraging **Machine Learning (Random Forest Algorithm)** and a structured **medical dataset**, this tool predicts the **top three most likely diseases** a user might have. Additionally, it provides a **Diabetes Risk Assessment**, calculating the probability of a user being diabetic based on key health indicators.

## Features
- **Symptom-Based Disease Prediction** - Users select symptoms, and the AI predicts possible diseases.
- **Diabetes Risk Calculator** - Users enter health parameters to get a probability score.
- **Fast & Efficient** - Predictions are generated in real-time.
- **User-Friendly Web Interface** - Built using Flask, HTML, and Python.
- **Privacy Focused** - No personal data is stored; all calculations happen instantly.

## Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning Model:** Random Forest Classifier
- **Dataset:** CSV files containing symptom-disease mappings and diabetic indicators

## How It Works
### **1️ Symptom-Based Diagnosis**
1. The user selects symptoms from a dynamically generated list.
2. The ML model processes the inputs and identifies the **top three most probable diseases**.
3. The results are displayed with relevant health insights.

### **2️ Diabetes Risk Prediction**
1. The user enters key health metrics (glucose level, BMI, age, etc.).
2. The AI calculates the probability of diabetes.
3. The result is displayed, indicating whether the user is at risk.

## Installation & Setup
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/sahnana-athota/diagnostic-assistant.git
cd diagnostic-assistant
```

### **Step 4: Run the Application**
```bash
python app.py
```

### **Step 5: Open in Browser**
```
http://127.0.0.1:5000
```

---

## Demo

https://github.com/user-attachments/assets/39e67b42-8c52-4678-8b53-dfdda042f2fc



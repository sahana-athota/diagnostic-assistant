# 🏥 Diagnostic Assistant - AI-Powered Disease Prediction

## 🚀 Overview
**Diagnostic Assistant** is an AI-driven web application that enables users to self-diagnose potential diseases based on their symptoms. By leveraging **Machine Learning (Random Forest Algorithm)** and a structured **medical dataset**, this tool predicts the **top three most likely diseases** a user might have. Additionally, it provides a **Diabetes Risk Assessment**, calculating the probability of a user being diabetic based on key health indicators.

## ✨ Features
- 🔍 **Symptom-Based Disease Prediction** - Users select symptoms, and the AI predicts possible diseases.
- 📊 **Diabetes Risk Calculator** - Users enter health parameters to get a probability score.
- ⚡ **Fast & Efficient** - Predictions are generated in real-time.
- 🌐 **User-Friendly Web Interface** - Built using Flask, HTML, and JavaScript.
- 🔐 **Privacy Focused** - No personal data is stored; all calculations happen instantly.

## 🛠️ Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning Model:** Random Forest Classifier
- **Dataset:** CSV files containing symptom-disease mappings and diabetic indicators

## 🎯 How It Works
### **1️⃣ Symptom-Based Diagnosis**
1. The user selects symptoms from a dynamically generated list.
2. The ML model processes the inputs and identifies the **top three most probable diseases**.
3. The results are displayed with relevant health insights.

### **2️⃣ Diabetes Risk Prediction**
1. The user enters key health metrics (glucose level, BMI, age, etc.).
2. The AI calculates the probability of diabetes.
3. The result is displayed, indicating whether the user is at risk.

## 📌 Installation & Setup
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/diagnostic-assistant.git
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

## 📂 Project Structure
```
├── static/                  # CSS, JavaScript, Images
├── templates/               # HTML templates
├── model/                   # Machine Learning models
├── app.py                   # Main Flask application
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## 📊 Future Improvements
- 📡 **API Integration** for real-time medical updates.
- 🏥 **Telemedicine Integration** for direct doctor consultations.
- 🤖 **Deep Learning Models** for improved accuracy.
- 📱 **Mobile App Version** for broader accessibility.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

## 🎉 Acknowledgments
Special thanks to **[Your Name]** for developing this project as part of the **2025 Girl Hackathon**! 🚀

---

🌐 **Live Demo:** [Insert Link Here]

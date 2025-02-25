from flask import *

import numpy as np
import pandas as pd
from modd import mod
from diabetes import predict_Diabetes_disease
app = Flask(__name__)

df = pd.read_csv("symbipredict_2022.csv")  
model = mod() 

symptom_columns = df.columns[:-1] 

def predict_disease(user_symptoms):
    input_data = np.zeros(len(symptom_columns))  # Initialize with zeros
    for symptom in user_symptoms:
        if symptom in symptom_columns:
            input_data[list(symptom_columns).index(symptom)] = 1  # Set corresponding symptom to 1

    probabilities = model.predict_proba([input_data])[0]
    disease_probabilities = dict(zip(model.classes_, probabilities))
    sorted_diseases = sorted(disease_probabilities.items(), key=lambda x: x[1], reverse=True)

    return sorted_diseases[:3]



@app.route("/symptoms", methods=["GET", "POST"])
def symptoms():
    if request.method == "POST":
        if request.form["home"]!="back":
            symptoms = request.form.getlist("symptoms")
            if(symptoms and symptoms!=['']): 
                predicted_diseases = predict_disease(symptoms)
                return render_template("disease_symptom.html", symptoms=symptom_columns, result=predicted_diseases)
            else:
                return render_template("disease_symptom.html", symptoms=symptom_columns, result=None)
        else:
            return redirect(url_for("home"))


    return render_template("disease_symptom.html", symptoms=symptom_columns, result=None)


@app.route("/", methods=["GET","POST"])
def main():
    return redirect(url_for("home"))
    
@app.route("/home", methods=["GET","POST"])
def home():
    if request.method == "POST":
        if request.form["page"]=="symptoms":
            return redirect(url_for("symptoms"))
        else:
            return redirect(url_for("diabetes"))
    return render_template("main.html")



@app.route("/diabetes", methods=["GET", "POST"])
def diabetes():
    if request.method == "POST":
        if request.form["home"]!="back":
            user_input = {
                "gender": request.form["gender"],
                "age": int(request.form["age"]),
                "hypertension": int(request.form["hypertension"]),
                "heart_disease": 1 if request.form["heart_disease"] == "Yes" else 0,
                "bmi": float(request.form["bmi"]),
                "smoking_history": request.form["smoking_history"],
                "HbA1c_level": float(request.form["HbA1c_level"]),
                "blood_glucose_level": float(request.form["blood_glucose_level"]),
            }
            result_text, probability=predict_Diabetes_disease(user_input)
            return render_template("diabetes.html", result=result_text, probability=f"{probability:.2f}")
        else:
            return redirect(url_for("home"))

    return render_template("diabetes.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from modd import mod

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




@app.route("/", methods=["GET", "POST"])
def index():
    print(request.form.getlist("symptoms"))
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")
        print(symptoms)
        if(symptoms and symptoms!=['']): 
            predicted_diseases = predict_disease(symptoms)
            return render_template("index.html", symptoms=symptom_columns, result=predicted_diseases)
        else:
            return render_template("index.html", symptoms=symptom_columns, result=None)


    return render_template("index.html", symptoms=symptom_columns, result=None)




if __name__ == "__main__":
    app.run(debug=True)

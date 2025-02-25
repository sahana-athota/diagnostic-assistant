import os
import re
import pytesseract
from PIL import Image
import pdf2image 
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("here",text)
    return text

def extract_text_from_pdf(pdf_path):
    images = pdf2image.convert_from_path(pdf_path)
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)
    print("here",text)
    return text

def extract_patient_info(text):
    patient_info = {}
    
    age_pattern = r"Age:\s*(\d+)"
    age_match = re.search(age_pattern, text)
    if age_match:
        patient_info['Age'] = int(age_match.group(1))
    x = re.findall("HEMOGLOBIN.*g/dl", text)
    print("HERE",x)
    patterns = {
        "HEMOGLOBIN":r"HEMOGLOBIN.*g/dl",
        "NEUTROPHILS":r"NEUTROPHILS.*%" ,
        "EOSINOPHILS":r"EOSINOPHILS.*%" ,
        "HYPERTENSION":r"HYPERTENSION.*%" ,
        "BLOOD GLUCOSE":r"BLOOD GLUCOSE.*%"
    }





    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        
        if match:
            print("match",match)
            m=re.findall(pattern,text)
            m=m[0].split()[1]
            patient_info[key]=float(m)
    print("over heree",patient_info)
    return patient_info

def assess_risk(patient_info):
    risk_results = {}
    age = patient_info.get("Age", 30)  
    
    reference_ranges = {
        "HEMOGLOBIN": (13.5, 17.5) if age >= 18 else (11.5, 15.5),
        "EOSINOPHILS": (1,6),
        "NEUTROPHILS":(40,80),
        "HYPERTENSION":(20,300),
        "BLOOD GLUCOSE":(20,300)
    }
    
    for test, value in patient_info.items():
        if test in reference_ranges:
            low, high = reference_ranges[test]
            if value < low:
                risk_results[test] = "Low - Possible deficiency"
            elif value > high:
                risk_results[test] = "High - Possible health risk"
            else:
                risk_results[test] = "Normal"
    
    return risk_results

def predict_disease(risk_results):
    disease_risks = {
        "Anemia": ["HEMOGLOBIN"],
        "Infection": ["EOSINOPHILS"],
        "Heart Disease": ["NEUTROPHILS"],
        "abc":["HYPERTENSION"],
        "def":["BLOOD GLUCOSE"]
    }
    
    predicted_diseases = []
    
    for disease, factors in disease_risks.items():
        for factor in factors:
            if factor in risk_results and "High" in risk_results[factor]:
                predicted_diseases.append(disease)
                break
    
    return predicted_diseases

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template("upload.html", message="No file part")
        file = request.files["file"]
        if file.filename == '':
            return render_template("upload.html", message="No selected file")
        if file and allowed_file(file.filename):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            if file.filename.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(filepath)
            else:
                extracted_text = extract_text_from_image(filepath)
            
            patient_info = extract_patient_info(extracted_text)
            risk_results = assess_risk(patient_info)
            predicted_diseases = predict_disease(risk_results)
            
            return render_template("results.html", 
                                   patient_info=patient_info, 
                                   risk_results=risk_results, 
                                   predicted_diseases=predicted_diseases)
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

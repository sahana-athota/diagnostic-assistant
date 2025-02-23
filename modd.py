import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def mod():
    df = pd.read_csv("symbipredict_2022.csv")  

    X = df.iloc[:, :-1]  
    y = df.iloc[:, -1]  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(
        n_estimators=200,
        class_weight='balanced',
        max_depth=5, 
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return model

'''
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print("Classification Report:")
print(classification_report(y_test, y_pred))

def predict_disease(user_symptoms):
    input_data = np.zeros(len(X.columns))  # Initialize with zeros
    
    for symptom in user_symptoms:
        if symptom in X.columns:
            input_data[X.columns.get_loc(symptom)] = 1  
    

    probabilities = model.predict_proba([input_data])[0]

    disease_probabilities = {disease: prob for disease, prob in zip(model.classes_, probabilities)}
    sorted_diseases = sorted(disease_probabilities.items(), key=lambda x: x[1], reverse=True)
    
    print("Top 3 probable diseases:")
    for disease, probability in sorted_diseases[:3]:
        print(f"{disease}: {probability * 100:.2f}%")
    
    return sorted_diseases[:3]


predict_disease(["chills", "depression","fatigue","anxiety","weight_gain","blurred_and_distorted_vision"])
'''

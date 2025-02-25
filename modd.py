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

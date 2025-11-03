import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import joblib


try:
    data = pd.read_csv('dataset.csv')

except FileNotFoundError:
    print("The dataset was not found.")
    exit()

print("Dataset Loaded Successfully.")


X= data.drop('label', axis=1)
y= data['label']
print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Data split into training ({len(X_train)} rows ) and testing sets ({len(X_test)} rows) sets. \n")

print(" Training Model : Using Decision Tree Classifier")
dt_model = DecisionTreeClassifier(random_state=42)


dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

accuracy_score_dt = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Classifier Accuracy: {accuracy_score_dt*100:.2f}%")
print("Classification Report:\n", classification_report(y_test, y_pred_dt))


print(" Training Model : Using Random Forest Classifier")
rf_model = RandomForestClassifier(n_estimators=100 ,random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
accuracy_score_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Classifier Accuracy: {accuracy_score_rf*100:.2f}%")
print("Classification Report:\n", classification_report(y_test, y_pred_rf))

print("----Best Model----")
if accuracy_score_rf > accuracy_score_dt:
    best_model = rf_model
    model = 'RF.joblib'
    print(f"Random Forest Classifier selected with accuracy: {accuracy_score_rf*100:.2f}%")

else:
    best_model = dt_model
    model = 'DT.joblib'
    print(f"Decision Tree Classifier selected with accuracy: {accuracy_score_dt*100:.2f}%")


joblib.dump(best_model, model)
print(f"{model} saved successfully.")


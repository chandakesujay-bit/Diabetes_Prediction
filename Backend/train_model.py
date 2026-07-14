import pandas as pd

df = pd.read_csv("dataset/diabetes.csv")

print(df.head())

print(df.info())

print(df.describe())
print(df.isnull().sum())
print((df == 0).sum())

cols = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in cols:
    df[col] = df[col].replace(0, df[col].median())

# Check again after replacing zeros
print((df == 0).sum())

# Step 6: Split Features and Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

print(X.head())
print(y.head())
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

print("Model trained successfully!")
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
import joblib

joblib.dump(model, "model/diabetes_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model and scaler saved successfully!")
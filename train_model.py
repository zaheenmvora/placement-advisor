import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("data/training_data.csv")

X = df.drop("domain", axis=1)
y = df["domain"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = RandomForestClassifier()
model.fit(X, y_encoded)

# Save model and encoder
joblib.dump(model, "ml_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Model trained and saved successfully!")

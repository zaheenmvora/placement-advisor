import joblib
import numpy as np

model = joblib.load("ml_model.pkl")
le = joblib.load("label_encoder.pkl")

def predict_domain_ml(profile):

    features = np.array([[
        profile["dsa"],
        profile["python"],
        profile["web"],
        profile["ml"],
        profile["os"],
        profile["dbms"],
        profile["cgpa"]
    ]])

    probabilities = model.predict_proba(features)[0]

    domain_probs = {
        le.inverse_transform([i])[0]: float(prob)
        for i, prob in enumerate(probabilities)
    }

    best_domain = max(domain_probs, key=domain_probs.get)

    return {
        "recommended_domain_ml": best_domain,
        "probabilities": domain_probs
    }

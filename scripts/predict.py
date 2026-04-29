import pickle
import pandas as pd

# Load trained model
with open("finance_risk_model.pkl", "rb") as f:
    model = pickle.load(f)

# ===== INPUT DATA (UPDATE VALUES AS NEEDED) =====
input_data = {
    'customerid': 1,
    'quantity_x': 0.5,
    'unitprice_x': 1.2,
    'absolutequantity': 0.3,
    'unitprice_y': 0.7,
    'salesamount_x': 1.1
    # Add remaining features if needed
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Ensure all required features are present
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Arrange columns in correct order
input_df = input_df[model.feature_names_in_]

# Prediction
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# Output
print("Prediction:", prediction)
print("Risk:", "High Risk 🚨" if prediction == 1 else "Low Risk ✅")
print("Confidence:", round(probability * 100, 2), "%")
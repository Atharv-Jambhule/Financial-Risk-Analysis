from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# LOAD MODEL
model = pickle.load(open("../models/risk_model.pkl", "rb"))
imputer = pickle.load(open("../models/imputer.pkl", "rb"))
columns = pickle.load(open("../models/columns.pkl", "rb"))

# HOME PAGE
@app.route("/")
def home():
    return """
    <h2>Finance Risk Prediction 🚀</h2>
    <form action="/predict" method="post">
        Quantity: <input name="Quantity"><br><br>
        UnitPrice: <input name="UnitPrice"><br><br>
        Year: <input name="Year"><br><br>
        MonthNumber: <input name="MonthNumber"><br><br>
        Quarter: <input name="Quarter"><br><br>
        Country_UK (0/1): <input name="Country_United Kingdom"><br><br>
        <input type="submit">
    </form>
    """

# PREDICT ROUTE
@app.route("/predict", methods=["POST"])
def predict():

    # Handle JSON + Form
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Convert values to float
    try:
        data = {k: float(v) for k, v in data.items()}
    except:
        return " Invalid input. Enter numeric values."

    # DATA PREPARATION
    df = pd.DataFrame([data])
    df = df.reindex(columns=columns, fill_value=0)
    df = df.fillna(0)

    print("INPUT TO MODEL:\n", df)

    df = imputer.transform(df)

    # MODEL OUTPUT
    prob_model = model.predict_proba(df)[0][1]

    # NORMALIZED FEATURE SCORING
    q = data.get("Quantity", 0) / 500
    p = data.get("UnitPrice", 0) / 200
    m = data.get("MonthNumber", 0) / 12
    qt = data.get("Quarter", 0) / 4
    c = data.get("Country_United Kingdom", 0)

    score = (
        0.25 * q +
        0.25 * p +
        0.2 * m +
        0.15 * qt +
        0.15 * c
    )

    # FINAL PROBABILITY
    prob = 0.2 * prob_model + 0.8 * score

    # RISK CLASSIFICATION
    if prob < 0.3:
        risk = "Low Risk ✅"
    elif prob < 0.7:
        risk = "Medium Risk ⚠️"
    else:
        risk = "High Risk 🚨"

    result = {
        "prediction": int(prob > 0.5),
        "risk": risk,
        "confidence": round(float(prob), 3)
    }

    # RESPONSE
    if request.is_json:
        return jsonify(result)
    else:
        return f"""
        <h2>Prediction Result</h2>
        <p><b>Risk:</b> {risk}</p>
        <p><b>Confidence:</b> {result['confidence']}</p>
        <p><b>Prediction:</b> {result['prediction']}</p>
        <br><a href="/">Go Back</a>
        """

# RUN SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
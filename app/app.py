from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# LOAD PRODUCT DATA
df_product = pickle.load(open("../models/product_data.pkl", "rb"))

@app.route("/")
def home():
    return "Product Risk API Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    try:
        quantity = float(data["Quantity"])
        price = float(data["UnitPrice"])
        year = int(data["Year"])
        month = int(data["MonthNumber"])
        quarter = int(data["Quarter"])
        country = int(data["Country_United Kingdom"])
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    input_amount = quantity * price

    low, medium, high = [], [], []

    for _, row in df_product.iterrows():

        product_amount = row["TotalAmount"]
        product_price = row["UnitPrice"]

        score = (
            0.4 * (input_amount / 100000) +
            0.3 * (product_amount / 100000) +
            0.3 * (product_price / 200)
        )

        if score < 0.4:
            low.append(row["Description"])
        elif score < 0.7:
            medium.append(row["Description"])
        else:
            high.append(row["Description"])

    return jsonify({
        "Low Risk": low,
        "Medium Risk": medium,
        "High Risk": high
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
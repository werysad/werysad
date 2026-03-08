from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "House Price Prediction API Running"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = request.args or (request.get_json(silent=True) or {})
    square_feet = data.get("SquareFeet")
    bedrooms = data.get("Bedrooms")
    if square_feet is None or bedrooms is None:
        return jsonify({"error": "SquareFeet and Bedrooms are required"}), 400

    features = [float(square_feet), float(bedrooms)]

    price = model.predict([features])
    return jsonify({"Predicted Price": float(price[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
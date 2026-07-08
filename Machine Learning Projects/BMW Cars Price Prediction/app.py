# pip install flask
# pip install pandas
# pip install joblib
# pip install scikit-learn==1.6.1
# Installing required libraries before running the application

from flask import Flask, request, jsonify
import pandas as pd
import joblib

model = joblib.load("bmw_price_model.pkl")

df = pd.read_csv("bmw_cars_market_dataset_cleaned.csv")

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "BMW Car Price Prediction API",
        "endpoints": {
            "GET /car/<car_id>": "Get car details by ID",
            "POST /predict": "Predict BMW car price"
        }
    })


@app.route("/car/<int:car_id>", methods=["GET"])
def get_car(car_id):

    car = df[df["car_id"] == car_id]

    if car.empty:
        return jsonify({
            "error": "Car ID not found."
        }), 404

    car = car.drop(columns=["price_usd"])

    return jsonify(car.iloc[0].to_dict())


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "No JSON data received."
            }), 400

        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]

        return jsonify({
            "Predicted Price (USD)": round(float(prediction), 2)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

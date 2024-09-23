from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("../models/co2_emission_estimator.joblib")

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict([data["features"]])
    return jsonify({"prediction":prediction[0]})

if __name__ == __main__:
    app.run(host="0.0.0.0", port=5000)
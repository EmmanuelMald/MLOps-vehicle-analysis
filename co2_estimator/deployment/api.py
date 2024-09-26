from flask import Flask, request, jsonify
import joblib
from pathlib import Path
import pandas as pd

INCLUDE_DIR = Path(__file__).parent.parent
MODEL_DIR = INCLUDE_DIR / "development/model/co2_emissions.joblib"
app = Flask(__name__)
model = joblib.load(MODEL_DIR)

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.get_json()
    data = pd.DataFrame(data["features"])
    prediction = model.predict(data)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
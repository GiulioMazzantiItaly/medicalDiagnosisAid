from flask import Flask, render_template, request, jsonify
from pathlib import Path
import joblib
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "diabetes_model.joblib"

app = Flask(__name__)
model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    feature_names = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]

    input_values = [float(request.form[name]) for name in feature_names]
    input_array = np.array(input_values).reshape(1, -1)

    prediction = int(model.predict(input_array)[0])
    probability = float(model.predict_proba(input_array)[0][1])

    return render_template(
        "result.html",
        prediction=prediction,
        probability=probability,
    )


# Adding a route API that accepts JSON input, and gives a JSON output
@app.route("/predict-json", methods=["POST"])
def predict_json():
    # Read JSON data from the request body
    data = request.get_json()

    # Keep the same feature order used during training
    feature_names = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]

    # Convert incoming values to a numeric NumPy array
    input_values = [float(data[name]) for name in feature_names]
    input_array = np.array(input_values).reshape(1, -1)

    # Generate prediction and probability
    prediction = int(model.predict(input_array)[0])
    probability = float(model.predict_proba(input_array)[0][1])

    # Return a JSON response
    return jsonify({
        "prediction": prediction,
        "probability": probability,
    })


if __name__ == "__main__":
    app.run(debug=True)
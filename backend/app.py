
import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize the Flask application
superkart_api = Flask("SuperKart Sales Predictor")

# Load the trained machine learning model
# We will use our trained model file
model = joblib.load("superkart_model.joblib")

@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart Sales Prediction API!"

@superkart_api.post('/v1/predict')
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    return jsonify({'Predicted Sales': round(float(prediction), 2)})

@superkart_api.post('/v1/predictbatch')
def predict_batch():
    file = request.files['file']
    input_data = pd.read_csv(file)
    predictions = model.predict(input_data).tolist()
    predictions = [round(float(p), 2) for p in predictions]
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    superkart_api.run(debug=True)

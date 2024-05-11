"""
    Flask API for serving predictions from a machine learning model.

    This module sets up a Flask application with a RESTful API endpoint `/predict`
    that accepts POST requests. The POST requests to this endpoint should contain
    JSON data which is then processed by a machine learning modelto return predic-
    tions. The application is designed to be scalable and can be deployed to any
    environment that supports Flask applications.

    Returns:
        _type_: _description_
"""
import os
from flask import Flask, request, jsonify
import numpy as np
import joblib

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

SAVE_MODEL_FOLDER = "models/"
SAVE_MODEL_FILENAME = "model.pkl"
MAX_SEQUENCE_LENGTH = 200
OOV_TOKEN = "-n-"

app = Flask(__name__)


def preprocess(data):
    tokenizer = Tokenizer(lower=True, char_level=True, oov_token=OOV_TOKEN)
    tokenizer.fit_on_texts(data)

    x= pad_sequences(
        tokenizer.texts_to_sequences(data), maxlen=MAX_SEQUENCE_LENGTH
    )
    
    return x

def load_model():
    """
    Loads model from Google Drive to query from.
    """

    model = joblib.load(f'{SAVE_MODEL_FOLDER}{SAVE_MODEL_FILENAME}')
    
    return model
    
model = load_model()

@app.route('/predict', methods=['GET'])
def info():
    """
    Predict endpoint.

    Returns:
        result (json) : JSON response.
    """
    result = jsonify({
        'msg': 'GET Request is Not Supported.'
    })
    return result

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict endpoint.

    Returns:
        result (json) : JSON response.
    """
    data = request.json['data']
    preprocessed_data = preprocess(data)
    prediction = model.predict(preprocessed_data)
    prediction = np.array(prediction > 0.5).astype(int)
    result = jsonify({'prediction': prediction.flatten().tolist()})
    return result


if __name__ == '__main__':
    app.run(debug=True)

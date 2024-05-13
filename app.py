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
from flask import Flask, request, jsonify
import numpy as np
import joblib
import gdown
import os 

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from ml_lib_remla.preprocessing import Preprocessing


SAVE_MODEL_FOLDER = "models/"
SAVE_MODEL_FILENAME = "model.joblib"
MAX_SEQUENCE_LENGTH = 200
OOV_TOKEN = "-n-"

app = Flask(__name__)

def load_model():
    """
    Loads model from Google Drive to query from.
    """
    
    if not os.path.exists(SAVE_MODEL_FOLDER):
        os.mkdir(SAVE_MODEL_FOLDER)

    model = joblib.load(gdown.download(id="1e1FyntLFwb1heG-_64uzxktGtGiD-kHs", output=f'{SAVE_MODEL_FOLDER}{SAVE_MODEL_FILENAME}', quiet=False))
    
    return model
    
model = load_model()
preprocessor = Preprocessing()

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict endpoint.

    Returns:
        result (json) : JSON response.
    """
    data = request.json['data']

    preprocessed_data = preprocessor.tokenize_batch(data)
    prediction = model.predict(preprocessed_data)
    prediction = np.array(prediction > 0.5).astype(int)
    result = jsonify({'prediction': prediction.flatten().tolist()})
    return result


if __name__ == '__main__':
    app.run(debug=True)

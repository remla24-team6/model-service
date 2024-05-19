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
import csv
from flasgger import Swagger, LazyJSONEncoder
from flasgger import swag_from
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.flaskenv')
load_dotenv(dotenv_path=env_path)

from ml_lib_remla.preprocessing import Preprocessing

from config import SWAGGER_TEMPLATE, SWAGGER_CONFIG


app = Flask(__name__)
app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, template=SWAGGER_TEMPLATE,config=SWAGGER_CONFIG)

class Inference():
    """
    Loads model from Google Drive to query from.
    """
    def __init__(self):
        """
        Initialises model from Google Drive.
        """
    
        if not os.path.exists(os.getenv('SAVE_MODEL_FOLDER')):
            os.mkdir(os.getenv('SAVE_MODEL_FOLDER'))

        self.model = joblib.load(gdown.download(id=os.getenv('GDRIVE_ID'), output=f'{os.getenv("SAVE_MODEL_FOLDER")}{os.getenv("SAVE_MODEL_FILENAME")}', quiet=False))        
    
@swag_from("docs/predict.yaml" )
@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict endpoint.

    Returns:
        result (json) : JSON response.
    """
    data = request.json['data']

    preprocessed_data = preprocessor.tokenize_batch(data)
    prediction = inference.model.predict(preprocessed_data)
    prediction = np.array(prediction > 0.5).astype(int)
    result = jsonify({'prediction': prediction.flatten().tolist()})
    return result


@swag_from("docs/add.yaml" )
@app.route('/add', methods=['POST'])
def add():
    """
    Add training data.

    Returns:
        result (json) : JSON response.
    """
    url = request.json['url']
    label = request.json['label']

    # Path to the CSV file
    csv_file_path = f"{os.getenv('SAVE_TRAINING_DATA_FOLDER')}{os.getenv('SAVE_TRAINING_DATA_FILENAME')}"

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Append data to the CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([url, label])

    return jsonify({'msg': f'Thank you for submitting:\n{url} with label {label}'})

inference = Inference()
preprocessor = Preprocessing()

if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=os.getenv('IS_DEBUG'))

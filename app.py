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
from flasgger import Swagger, LazyJSONEncoder
from flasgger import swag_from


from ml_lib_remla.preprocessing import Preprocessing

from config import swagger_template, swagger_config
from constants import GDRIVE_ID

SAVE_MODEL_FOLDER = "models/"
SAVE_MODEL_FILENAME = "model.joblib"

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, template=swagger_template,config=swagger_config)

class Inference():
    """
    Loads model from Google Drive to query from.
    """
    def __init__(self):
        """
        Initialises model from Google Drive.
        """
    
        if not os.path.exists(SAVE_MODEL_FOLDER):
            os.mkdir(SAVE_MODEL_FOLDER)

        self.model = joblib.load(gdown.download(id=GDRIVE_ID, output=f'{SAVE_MODEL_FOLDER}{SAVE_MODEL_FILENAME}', quiet=False))        
    
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


inference = Inference()
preprocessor = Preprocessing()

if __name__ == '__main__':
    app.run(debug=True)

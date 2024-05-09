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

app = Flask(__name__)


class DummyModel:
    """
    Class to interface with the ML-model.
    """
    def predict(self, X):
        """
        Predicts outcome based on input data.
        """
        return 1

@app.route('/predict', methods=['GET'])
def info():
    """
    Predict endpoint.

    Returns:
        result (json) : JSON response.
    """
    result = jsonify({
        'msg': 'Not supported'
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
    prediction = DummyModel.predict(data)
    result = jsonify({'prediction': prediction.tolist()})
    return result


if __name__ == '__main__':
    app.run(debug=True)

swagger_template ={
    "swagger": "2.0",
    "info": {
      "title": "Phishing URL Prediction",
      "description": "API Documentation for Phshing URL Prediction",
      "contact": {
        "name": "Admin",
        },
      "termsOfService": "Terms of services",
      "version": "1.0",
      "host":"model-service",
      "basePath":"http://localhost:5000",
      "license":{
        "name":"License of API",
        "url":"API license URL"
      }
              },
    "schemes": [
        "http",
        "https"
    ],
      }

swagger_config = {
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST"),
    ],
    "specs": [
        {
            "endpoint": 'model_service',
            "route": '/phishing_url_prediction.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    
}




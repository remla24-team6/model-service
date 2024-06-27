# Model-service

Model-service repository for TU DELFT CS4295 Release Engineering for Machine Learning Applications (2023/24 Q4).

The model-service represents a wrapper service for the released ML model. It will offer a Flask REST API
to expose the model to other components and make it scalable. The trained model is fetched from the google drive upon startup. For preprocessing, the ml-lib library is used. On every push with a release tag, this repo should automatically be packaged and released.

### Setup
- Create a new virtual environment called `.venv` using `virtualenv .venv`
- Activate the virtual environment you just created using `source <path-to-env>/bin/activate`
- Install [Poetry](https://python-poetry.org/docs/) using `pip install poetry`.
- Install dependencies using poetry by running `poetry install`.

## API Configuration
To run the model-service locally or when building the Dockerfile, create a `.flaskenv` file containing:

``` file
IS_DEBUG=               (default: False)
HOST=                   (default: 0.0.0.0)
PORT=                   (default: 5000)
GDRIVE_ID=              (default: "1e1FyntLFwb1heG-_64uzxktGtGiD-kHs")
SAVE_MODEL_FOLDER=      ("models/")
SAVE_MODEL_FILENAME=    ("model.joblib")
```



## Installation instructions

1. Clone the repository.

```
$ git clone git@github.com:remla24-team6/model-service.git
$ cd model-service
```

2. To load from the GitHub Package registry:

``` console
docker pull ghcr.io/remla24-team6/model-service:latest
docker run -p 5000:5000 --name model-service -it ghcr.io/remla24-team6/model-service:latest
```

2. To build the docker container locally.

```
$ docker-compose build --no-cache
```

2. To run the docker container.

```
$ docker compose up (-d)
```

3. To close the docker container.

```
$ docker compose down
```

## API Usage

1. Go to [http://localhost:5000/apidocs](http://localhost:5000/apidocs) to find the API documentation.

### POST Request: Predict
A `/predict` POST request has the following body 

``` json
{
    "data": ["<URL>"]
}
```
The response body contains the following:

``` json
{
  "prediction": <0|1>
}
```

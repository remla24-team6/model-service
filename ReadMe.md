# Model-service

Model-service repository for TU DELFT CS4295 Release Engineering for Machine Learning Applications (2023/24 Q4)

The model-service represents a wrapper service for the released ML model. It will offer a REST API
to expose the model to other components and make it scalable.

## Installation instructions

1. Clone the repository.

```
$ git clone git@github.com:remla24-team6/model-service.git
$ cd model-service
```

2. Run the docker container

```
$ docker compose up (-d)
```

3. Close the docker container

```
$ docker compose down
```

FROM python:3.11-slim as python-base

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

# Create a new stage from the base python image
FROM python-base as model-service

# Copy Application
COPY . /app

# Run Application
EXPOSE 5000

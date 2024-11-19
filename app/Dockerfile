# Use an official Python runtime as a parent image
FROM python:3.12.7-alpine

# Install Updates
RUN apk update && apk upgrade --no-cache

# Install Poetry
RUN pip install poetry

# Install build dependencies
RUN apk add --no-cache \
    g++ \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    make \
    geos \
    geos-dev


# Copy the pyproject.toml and poetry.lock files

COPY pyproject.toml poetry.lock* /

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root --only main

# Copy the current directory contents into the container at /app
COPY . /app

# Port 8000
EXPOSE 8000

# Run app.py when the container launches
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

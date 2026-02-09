# ----------------- Stage: 1 - Builder Stage----------------- #

# Base image as python:3.13-slim
FROM python:3.13-slim AS builder

# Setting Working directory as app
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# ----------------- Stage: 2 - Runtime Stage ----------------- #

# Base image as python:3.13-slim
FROM python:3.13-slim

# Working directory as app
WORKDIR /app

# Copying the installations from the builder and the app from the local
COPY --from=builder /install /usr/local

COPY app ./app

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
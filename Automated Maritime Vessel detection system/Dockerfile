# Use a lightweight, official Python image optimized for production
FROM python:3.10-slim

# Install system-level dependencies required by openCV and geospatial libraries
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglx-mesa0 \
    && rm -rf /var/lib/apt/lists/*

# Set up the internal workspace directory inside the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your production script and trained weights file into the image
COPY production_inference.py .
COPY runs/detect/train/weights/best.pt ./best.pt

# Define what command the container runs when it boots up
ENTRYPOINT ["python", "production_inference.py"]

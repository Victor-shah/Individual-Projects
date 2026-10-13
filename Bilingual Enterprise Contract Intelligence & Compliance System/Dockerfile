# Use a lightweight official Python footprint optimized for ML deployments
FROM python:3.10-slim

# Set environment optimizations for Python performance inside Docker execution
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/app

WORKDIR /app

# Install native OS dependencies required for structural scientific builds (FAISS / PyTorch requirements)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements sheet to leverage Docker cache layers efficiently
COPY requirements.txt .

# Install ML framework dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all application resources into the container workspace
COPY . .

# Expose production target ports matching the FastAPI app runtime layer
EXPOSE 8000

# Run service using high-performance ASGI server configs
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

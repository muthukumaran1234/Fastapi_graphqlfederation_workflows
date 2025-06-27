# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the worker code
COPY . .

# Default command to run the worker
CMD ["python", "worker.py"]

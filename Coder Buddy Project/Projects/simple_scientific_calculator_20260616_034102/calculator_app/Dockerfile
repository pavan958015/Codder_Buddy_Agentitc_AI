# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if any are needed for your specific app, e.g., build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your application runs on (e.g., 8000 for Flask/FastAPI)
EXPOSE 8000

# Command to run the application. Adjust this based on your entry point (e.g., app:app or main.py)
CMD ["python", "backend/main.py"]
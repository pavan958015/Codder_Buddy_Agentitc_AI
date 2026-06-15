# Dockerfile for FastAPI Backend Service

# --- Stage 1: Build and Run ---
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if needed (e.g., for some database drivers)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install Python dependencies
# Use --no-cache-dir to keep the image size smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./src /app/src
COPY ./main.py /app/main.py
# If you have other necessary files (like database migrations, static files), copy them here too.

# Expose the port the app runs on (default for FastAPI is often 8000)
EXPOSE 8000

# Command to run the application using Uvicorn
# Replace 'main:app' with your actual entry point if different
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
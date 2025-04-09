# Use official Python 3.13 slim image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Install pip and build dependencies
RUN apt-get update && apt-get install -y gcc

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the FastAPI application code
COPY . .

# Expose the port used by the app
EXPOSE 8080

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

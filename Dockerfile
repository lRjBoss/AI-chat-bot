# Use slim Python image
FROM python:3.9-slim

# Install system packages needed to build tgcrypto
RUN apt-get update && apt-get install -y gcc g++ build-essential && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot script
COPY bot.py .

# Run bot
CMD ["python", "bot.py"]

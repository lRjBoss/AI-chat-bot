FROM python:3.9-slim

# ✅ Fix: Install GCC and required build tools (necessary for tgcrypto)
RUN apt-get update && \
    apt-get install -y gcc build-essential python3-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# 📂 Working directory
WORKDIR /app

# 📥 Copy your repo files
COPY repo /app

# 📦 Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 🚀 Start the bot
CMD ["python", "bot.py"]

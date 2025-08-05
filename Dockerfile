FROM python:3.9-slim

# 🔧 Install required build tools (fix tgcrypto error)
RUN apt-get update && \
    apt-get install -y gcc build-essential python3-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# 👷 Set working directory
WORKDIR /app

# 📂 Copy project files
COPY repo /app

# 📦 Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

# 🚀 Run the bot
CMD ["python", "bot.py"]

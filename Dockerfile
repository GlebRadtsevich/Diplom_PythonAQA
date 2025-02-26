FROM python:3.12-slim

WORKDIR /app

COPY . .

# Utilities for downloading, unzipping and adding repository keys
RUN apt-get update && apt-get install -y wget unzip gnupg     # Download Google public key
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -     # Add Google Chrome repository to package sources
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list     # Install python dependencies
    && pip install --no-cache-dir -r requirements.txt     # Clear cache
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV HEADLESS=true

CMD ["python", "-m", "pytest"]

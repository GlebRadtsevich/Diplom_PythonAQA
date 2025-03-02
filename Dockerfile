FROM python:3.12-slim

WORKDIR /app

COPY . .

# Utilities for downloading, unzipping and adding repository keys
RUN apt-get update && apt-get install -y wget unzip gnupg     # Install python dependencies
    && pip install --no-cache-dir -r requirements.txt     # Install python dependencies
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*    # Clear cache

ENV HEADLESS=true

CMD ["python", "-m", "pytest"]
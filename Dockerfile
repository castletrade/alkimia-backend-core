# Production Dockerfile for Alkimia Backend
# Optimized for high-availability fintech environments

FROM python:3.11-slim-bullseye

# System dependencies for cryptography and networking
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/castle-trade/alkimia

# Install institutional-grade dependencies
COPY package.json .
COPY requirements.txt . 
# Note: requirements.txt is synthesized from package.json or manually maintained
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/ ./src/
COPY migrations/ ./migrations/

# Create non-root service user for security compliance
RUN useradd -m alkimiasvc
USER alkimiasvc

# Internal port for handling financial webhooks and API traffic
EXPOSE 8080

# Production runtime configuration
ENV PYTHONOPTIMIZE=1
ENV FLASK_ENV=production

# Execution entry point
CMD ["python", "src/api/stripe_integration.py"]

# ----------- Stage 1: Build Environment -----------
FROM python:3.13.3-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# ----------- Stage 2: Production Image -----------
FROM python:3.13.3-slim

WORKDIR /app

# Install system runtime dependencies
RUN apt-get update && apt-get install -y libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder stage
COPY --from=builder /usr/local /usr/local

# Copy app source code
COPY . .

# Expose port
EXPOSE 8000

# Run app with Uvicorn
CMD ["uvicorn", "djcrm.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
# ----------- Stage 1: Build Environment -----------
FROM python:3.13.3-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y gcc libpq-dev curl
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*


# Install pipenv
RUN pip install pipenv

# Copy Pipenv files first
COPY Pipfile .
COPY Pipfile.lock .

# Install Python packages to /install directory
RUN pipenv lock --requirements > requirements.txt
RUN mkdir /install
RUN pip install --prefix=/install -r requirements.txt


# ----------- Stage 2: Production Image -----------
FROM python:3.13.3-slim

WORKDIR /app

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Install system runtime dependencies
# RUN apt-get update && apt-get install -y libpq-dev curl
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*


# Copy app source code
COPY . .

# Expose port
EXPOSE 8000

# Run app with Uvicorn
CMD ["uvicorn", "djcrm.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

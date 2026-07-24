FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies for psycopg2 and other packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/scripts/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Set the default command
CMD ["gunicorn", "api.wsgi:application", "--bind", "0.0.0.0:8100"]

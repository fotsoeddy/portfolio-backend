#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Starting the server..."
# Execute the command passed to the container
exec "$@"

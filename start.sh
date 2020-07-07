#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Make database migrations
echo "Make database migrations main"
python manage.py makemigrations

# Make api migrations
echo "Make database migrations api"
python manage.py makemigrations api

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

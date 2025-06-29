#!/usr/bin/env bash
# exit on error
set -o errexit

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting build process..."

# Install dependencies
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Installing dependencies..."
pip install -r requirements.txt

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Collecting static files..."
python manage.py collectstatic --no-input

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Running migrations..."
python manage.py migrate

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Creating sample data..."
python manage.py create_sample_data

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Build complete!"
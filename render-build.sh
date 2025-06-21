#!/usr/bin/env bash
# exit on error
set -o errexit

echo "--- Starting build script ---"
echo "--- Running apt-get update and install ---"
apt-get update && apt-get install -y libpq-dev
echo "--- Finished apt-get ---"

pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate

# Add diagnostic commands
echo "--- Listing static directory before collectstatic ---"
ls -R static
echo "----------------------------------------------------"

python manage.py collectstatic --noinput

echo "--- Listing staticfiles directory after collectstatic ---"
ls -R staticfiles
echo "-------------------------------------------------------" 
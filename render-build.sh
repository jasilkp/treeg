#!/usr/bin/env bash
# exit on error
set -o errexit

# Diagnostic: Show current directory and files
echo "================ BUILD START ================"
pwd
echo "================ FILES IN ROOT =============="
ls -l

echo "--- Listing static directory before collectstatic ---"
ls -lR static || echo "[WARNING] static directory not found!"
echo "----------------------------------------------------"

# Clear staticfiles directory before collectstatic
rm -rf staticfiles/

# Install dependencies and migrate
echo "--- Installing dependencies and running migrations ---"
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate

echo "--- Running collectstatic ---"
python manage.py collectstatic --noinput

echo "--- Listing staticfiles directory after collectstatic ---"
ls -lR staticfiles || echo "[WARNING] staticfiles directory not found!"
echo "-------------------------------------------------------"

echo "================ BUILD END ================" 
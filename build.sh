#!/usr/bin/env bash
# exit on error
set -o errexit

apt-get update && apt-get install -y libpq-dev
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser_prod

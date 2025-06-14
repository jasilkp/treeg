#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py createsuperuser --noinput --username admin --email admin@example.com 
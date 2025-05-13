#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py createsuperuser --noinput --username admin --email admin@example.com 
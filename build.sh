#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser_prod
python manage.py collectstatic --noinput

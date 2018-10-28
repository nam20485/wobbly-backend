#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn backend.wsgi -c gunicorn_config.py
#!/bin/bash

python -Wall manage.py collectstatic --noinput

pytest
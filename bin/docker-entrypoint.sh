#! /bin/bash

SLEEP_SECONDS=3

>&2 echo "Checking Postgres status..."

# https://docs.docker.com/compose/startup-order/
export PGPASSWORD=$POSTGRES_PASSWORD
until psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -p "$POSTGRES_PORT" -d postgres -c '\q'
do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep $SLEEP_SECONDS
done
>&2 echo "Postgres is up"

python manage.py collectstatic --noinput

python manage.py migrate --noinput

gunicorn backend.wsgi -c gunicorn.conf.py
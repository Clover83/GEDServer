#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Not sure if this is a good idea in production,
# but I can't think of a reason it wouldn't be.
python manage.py makemigrations
python manage.py migrate

exec "$@"

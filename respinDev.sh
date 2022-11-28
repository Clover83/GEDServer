#!/bin/sh

docker-compose -f docker-compose.yml down -v
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput

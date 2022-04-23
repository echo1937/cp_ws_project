#!/usr/bin/env bash

python manage.py collectstatic --no-input
python manage.py migrate --no-input
gunicorn cp_ws_project.asgi:application -k uvicorn.workers.UvicornWorker -c ./deploy/gunicorn/gunicorn.py
#!/usr/bin/env bash
set -o errexit

# Render provides $PORT; default to 8000 for local runs
PORT_TO_BIND="${PORT:-8000}"

python -m gunicorn accounting.wsgi:application --bind "0.0.0.0:${PORT_TO_BIND}"

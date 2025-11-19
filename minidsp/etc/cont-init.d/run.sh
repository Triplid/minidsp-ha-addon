#!/usr/bin/with-contenv bash
# Этот скрипт запускается автоматически через s6-overlay при старте контейнера

echo "Starting miniDSP Python API..."
exec gunicorn --bind 0.0.0.0:8080 api:app

#!/usr/bin/with-contenv bash
echo "miniDSP API starting..."
# gunicorn запускаем через venv
exec /opt/venv/bin/gunicorn --bind 0.0.0.0:8080 api:app

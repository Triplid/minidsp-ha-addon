#!/usr/bin/with-contenv bash
# cont-init.d автоматически исполняется s6-overlay
echo "miniDSP API starting..."
# gunicorn запускаем через venv
/opt/venv/bin/gunicorn --bind 0.0.0.0:8080 api:app

#!/usr/bin/env bash
# /etc/cont-init.d/run.sh
set -e

echo "[miniDSP] Starting miniDSP 2x4HD Controller..."

# Активируем виртуальное окружение
source /opt/venv/bin/activate

# Запускаем gunicorn БЕЗ bash и БЕЗ with-contenv
# exec заменяет текущий процесс → gunicorn становится PID 1 → s6-overlay доволен
exec gunicorn --bind 0.0.0.0:8080 \
               --workers 2 \
               --worker-class sync \
               --log-level info \
               api:app

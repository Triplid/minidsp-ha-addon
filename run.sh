#!/usr/bin/env bash
set -e

# Небольшая задержка, чтобы система успела инициализировать usb
sleep 1

# Проверим есть ли бинарник minidsp
if ! command -v minidsp >/dev/null 2>&1; then
echo "minidsp CLI not found in PATH. Trying fallback location..."
if [ -f /root/.cargo/bin/minidsp ]; then
cp /root/.cargo/bin/minidsp /usr/local/bin/minidsp
fi
fi

# Лог запуска
echo "Starting miniDSP API (Flask)"
exec gunicorn --bind 0.0.0.0:8080 api:app

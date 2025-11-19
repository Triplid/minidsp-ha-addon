ARG BUILD_FROM=ghcr.io/hassio-addons/base:14.0.0
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-virtualenv bash

# создаём виртуальное окружение
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt

COPY api.py /app/api.py
COPY etc/cont-init.d/ /etc/cont-init.d/
RUN chmod a+x /etc/cont-init.d/*

WORKDIR /app
EXPOSE 8080

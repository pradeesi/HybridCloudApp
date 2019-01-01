FROM python:2.7.15-alpine3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install --no-cache-dir -r requirements.txt; \
	apk del .build-deps;

COPY . .

CMD [ "uwsgi", "--socket", "0.0.0.0:5061", "--protocol=http", "-w", "frontend:app" ]
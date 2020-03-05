FROM python:2.7.15-alpine3.8
#FROM python:2.7.15-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm mqtt_db_plugin.py
RUN rm mariadb_con_mqtt_db_plugin.py
RUN rm mqtt_db_plugin_backup.py
RUN rm test.py


CMD [ "python", "./mqtt_db_plugin.pyc" ]
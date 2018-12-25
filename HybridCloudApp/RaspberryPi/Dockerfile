FROM arm32v7/python:2.7.15-stretch

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y upgrade

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
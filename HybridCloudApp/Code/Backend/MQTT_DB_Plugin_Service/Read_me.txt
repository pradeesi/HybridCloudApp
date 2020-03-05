Create Docker Container Image- 
=================================

docker build -t mqtt_db_plugin .

docker image tag mqtt_db_plugin pradeesi/mqtt_db_plugin:v7

docker login

docker image push pradeesi/mqtt_db_plugin:v7






eu.gcr.io/fwardz001-poc-ci1s/
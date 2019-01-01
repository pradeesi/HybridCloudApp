Create Container Image using the following command - 
---------------------------------------------
sudo docker build -t rapi_cl_hc_sensor .


Login to Docker Public Registry using the following command - 
---------------------------------------------
sudo docker login


Tag your container image with Docker username using the following command -
---------------------------------------------
sudo docker image tag rapi_cl_hc_sensor pradeesi/rapi_cl_hc_sensor


Push the Container Image to Registry using the following command -
---------------------------------------------
sudo docker push pradeesi/rapi_cl_hc_sensor


Run container using the following command - 
---------------------------------------------
Interactive Mode - 
=================
sudo docker run --privileged -it -v /home/pi/settings:/usr/src/app/settings pradeesi/rapi_cl_hc_sensor

demon mode - 
============
sudo docker run --privileged -d -v /home/pi/settings:/usr/src/app/settings pradeesi/rapi_cl_hc_sensor

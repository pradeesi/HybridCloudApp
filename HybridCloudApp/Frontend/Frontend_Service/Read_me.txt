Export variable on MAC
=======================
export BACKEND_HOST=<backend service ip>
export BACKEND_PORT=<backend port>



Create Docker Container
========================
docker build -t frontend_server .


eu.gcr.io/fwardz001-poc-ci1s/


Run the Container 
===================
docker run -it -p 80:5061 -e BACKEND_HOST='35.228.248.122' -e BACKEND_PORT='80' frontend_server
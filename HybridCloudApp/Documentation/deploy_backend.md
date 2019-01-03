# Deploy Backend Application

## Objective:

In this section we would deploy the 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/backend_app_architecture.png)


## 1. Deploy MariaDB

### 1.1 Create Kubernetes Secret:

* **1.1.1: Create DB Password Secret**

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **1.1.2: Verify DB Password Secret**

		kubectl get secret mariadb-root-pass
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_root_pass.png)
	

### 1.2 Create PersistentVolume:

* **1.2.1: Create Persistent Volume** 

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_persistent_volume.yaml

* **1.2.2: Verfiy PersistentVolume**

		kubectl get pvc mariadb-pv-claim
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/pv_claim.png)
	
	>**Note:** It can take up to a few minutes for the PVs to be provisioned.
	
### 1.3 Deploy Database:

* **1.3.1: Deploy MariaDB**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_deployment.yaml
		
* **1.3.1: Check Deployment Status**

		kubectl get deployment iot-backend-mariadb
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/iot_backend_mariadb.png)
		
### 1.4 Create DB Service:

* **1.4.1: Expose MariaDB to other Pods**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_service.yaml
				
* **1.4.2: Verify Service Status**

		kubectl get service mariadb-service
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_service.png)


## 2. Deploy MQTT to DB Agent

* **2.1: Deploy MQTT to DB Agent**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/MQTT_DB_Agent/mqtt_db_agent_deployment.yaml


* **2.2: Check Deployment Status**

		kubectl get deployment iot-backend-mqtt-db-agent
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mqtt_db_agent.png)
	
		

## 3. Deploy REST API Agent


### 3.1 Deploy REST API Agent:
* **3.1.1: Deploy REST API Agent**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent.yaml

* **3.1.2: Check Deployment Status**

		kubectl get deployment iot-backend-rest-api-agent
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_agent.png)


### 3.2 Expose REST API Agent to Google Cloud using Kubernetes Service:

* **3.2.1: Create REST API Agent Service**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent_service_node_port.yaml

* **3.2.2: Check REST API Agent Service Status**

		kubectl get service rest-api-agent-service
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_agent_service.png)
	
### 3.3 Locate the IP and Port to Access Node-Port Service:

* Use the following command to display the port exposed by 'rest-api-agent-service' -

		kubectl get service rest-api-agent-service

* Use the following command to display the 'External-IP' of you kubernetes nodes -

		kubectl get nodes -o wide

	Following screenshot highlights the Port and Node IPs in the command outputs -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/node_port_service.png)

>**Important:** Note down the Node External IP Address and NodePort Service Port Number. These values would be used in next section for deploying the frontend app as the environment variables values ('**BACKEND\_HOST**' and '**BACKEND\_PORT**').

## 4 Test the REST API Agent Service:

To test the REST API service try to access following url from your web browser -

	http://<node's external ip>:30500/
	
If your REST API Agent is working properly, you should see 'Welcome to the API Service...!' message on your browser as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_url_test.png)

Following are the other urls that you could test -

	http://<node's external ip>:30500/cities
	
	http://<node's external ip>:30500/temperature
	
	http://<node's external ip>:30500/humidity
	
	http://<node's external ip>:30500/sensor_data/city
	
## Conclusion:

You have successfully deployed all the backend components of the iot-app on the CCP kubernetes cluster. Now you may proceed futher and deploy the frontend components on Google Cloud.







## 1. Deploy MariaDB

### 1.1 Create Kubernetes Secret:

* **1.1.1: Create DB Password Secret**

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **1.1.2: Verify DB Password Secret**

		kubectl get secret mariadb-root-pass

### 1.2 Create PersistentVolume:

* **1.2.1: Create Persistent Volume** 

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_persistent_volume.yaml

* **1.2.2: Verfiy PersistentVolume**

		kubectl get pvc mariadb-pv-claim
	
	**Note:** It can take up to a few minutes for the PVs to be provisioned.
	
### 1.3 Deploy Database:

* **1.3.1: Deploy MariaDB**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_deployment.yaml
		
* **1.3.1: Check Deployment Status**

		kubectl get deployment iot-backend-mariadb
		
### 1.4 Create DB Service:

* **1.4.1: Expose MariaDB to other Pods**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_service.yaml
				
* **1.4.2: Verify Service Status**

		kubectl get service mariadb-service


## 2. Deploy MQTT to DB Agent

* **2.1: Deploy MQTT to DB Agent**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/MQTT_DB_Agent/mqtt_db_agent_deployment.yaml


* **2.2: Check Deployment Status**

		kubectl get deployment iot-backend-mqtt-db-agent
		

## 3. Deploy REST API Agent


### 3.1 Deploy REST API Agent:
* **3.1.1: Deploy REST API Agent**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent.yaml

* **3.1.2: Check Deployment Status**

		kubectl get deployment iot-backend-rest-api-agent


### 3.2 Expose REST API Agent to Google Cloud using Kubernetes Service:

* **3.2.1: Create REST API Agent Service**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent_service_node_port.yaml

* **3.2.2: Check REST API Agent Service Status**

		kubectl get service rest-api-agent-service


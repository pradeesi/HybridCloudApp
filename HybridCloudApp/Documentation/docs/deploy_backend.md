# Deploy the Backend Application Components on CCP Kuberneted Cluster (Tenant Cluster)


In this section you would deploy the backend components of the IoT Application on the Kubernetes cluster deployed on your CCP instance. Following diagram shows the high-level architure of these backend application containers -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/backend_app_architecture.png)

SSH into your kubernetes master node and start deploying the components by following the instruction given below -

## 1. Deploy MariaDB Databse:

MariaDB will be used in the backend to save the sensor data recieved from AWS IoT platform over MQTT protocol. For this we would create following objects -

1. Kubernetes Secret
2. Kubernetes Persistent Volume Claim (PVC)
3. Kubernetes MariaDB Deployment
4. Kubernetes ClusterIP Service (Headless Service)

Following diagram shows the relationship between these objects -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_kubernetes_deployment.png)

### 1.1 Create Kubernetes Secret:

A **Kubernetes Secret** is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in an image; putting it in a Secret object allows for more control over how it is used, and reduces the risk of accidental exposure.

The MariaDB container image uses an environment varinable named as 'MYSQL\_ROOT\_PASSWORD', it hold the root password required to access the database. So you would create a new secret with 'password' key (value as 'cisco123') which would later be used in mariaDB deployment yaml file.

* **1.1.1: Create DB Password Secret -** Use the following command to create a new secret on your kubernetes cluster -

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **1.1.2: Verify DB Password Secret -** Check if the secret was created successfully or not -

		kubectl get secret mariadb-root-pass
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_root_pass.png)
	

### 1.2 Create Kubernetes Persistent Volume Claim:

A **Kubernetes Persistent Volume Claim (PVC)** is a request for storage by a user. It is similar to a pod. Pods consume node resources and PVCs consume Persistent Volume (PV) resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., can be mounted once read/write or many times read-only).

To keep the sensor data safe during Pod restarts, you would create a new Persistent Volume Claim. Following yaml definition would be used to create the 'PersistentVolumeClaim' - 

**(Question: How much storage 'mariadb-pv-claim' would use?)**

	---
	apiVersion: v1
	kind: PersistentVolumeClaim
	metadata:
	  name: mariadb-pv-claim
	  labels:
	    app: iot-backend
	spec:
	  accessModes:
	    - ReadWriteOnce
	  resources:
	    requests:
	      storage: 2Gi

* **1.2.1: Create Persistent Volume Claim -** Use the following command to create a new Persistent Volume Claim for MariaDB Pod -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_persistent_volume.yaml

* **1.2.2: Verfiy Persistent Volume Claim -** Check if the PVC was created successfully or not -

		kubectl get pvc mariadb-pv-claim
	
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/pv_claim.png)
	
>**Important:** It can take up to a few minutes for the PVs to be provisioned. DO NOT procced futher till the PVC deployment gets completed.
	
### 1.3 Deploy MariaDB on Kubernetes:

**MariaDB** is a community-developed fork of the MySQL relational database management system intended to remain free under the GNU GPL. Development is led by some of the original developers of MySQL, who forked it due to concerns over its acquisition by Oracle Corporation. MariaDB intends to maintain high compatibility with MySQL, ensuring a drop-in replacement capability with library binary parity and exact matching with MySQL APIs and commands.

* **1.3.1: Deploy MariaDB -** Use the following command to create a MariaDB kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_deployment.yaml
		
* **1.3.1: Check Deployment Status -** Use the following command to check if the kubernetes deployment was successfully created or not -

		kubectl get deployment iot-backend-mariadb
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/iot_backend_mariadb.png)
	
* **1.3.2: Check Pod Status -** Use the following command to check if the 'iot-backend-mariadb' pod is in '**Running**' state -

		kubectl get pods

> **Note:** Kubernetes may take some time to deploy the MariaDB. Do Not proceed further till the time DB Pod is up.	
		
### 1.4 Create Kubernetes ClusterIP Service:

Since the MariaDB will be accessed by other services like 'MQTT to DB Agent' and 'REST API Agent'; you need to expose it internally withing the kubernetes cluster using a Service using a Kubernetes 'ClusterIP' Service.

A **Kubernetes ClusterIP Service** is the default Kubernetes service. It gives you a service inside your cluster that other apps inside your cluster can access. There is no external access (For testing you could access ClusterIP service via Kubernetes Proxy Service, though it is not recommended).

Following yaml definition would be used to create the ClusterIP Service for MariaDB -

	---
	apiVersion: v1
	kind: Service
	metadata:
	  name: mariadb-service
	  labels:
	    app: iot-backend
	spec:
	  ports:
	    - protocol: TCP
	      port: 3306
	      targetPort: 3306
	  selector:
	    app: iot-backend
	    tier: mariadb
	  clusterIP: None



* **1.4.1: Expose MariaDB to other Pods -** Create a new kubernetes service using the following command -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_service.yaml
				
* **1.4.2: Verify Service Status -** Use the following command to check if the kubernetes service was deployed successfully or not -

		kubectl get service mariadb-service
		
	You should have the output similar to the following screenshot -
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_service.png)


## 2. Deploy MQTT to DB Agent:

'MQTT to DB Agent' will subscribe to the MQTT Topic and listen to the incomming sensor data from AWS IoT platform. It will then parse the sensor data and insert it into the MariaDB.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mqtt_db_agent_deployment.png)

* **2.1: Deploy MQTT to DB Agent -** Use the following command to create mqtt-to-db-agent kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/MQTT_DB_Agent/mqtt_db_agent_deployment.yaml


* **2.2: Check Deployment Status -** Use the following command to check if the kubernetes deployment was created successfully or not -

		kubectl get deployment iot-backend-mqtt-db-agent
		
	You should have the output similar to the following screenshot -
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mqtt_db_agent.png)
	
* **2.3: Check Pod Status -** Use the following command to check if the 'iot-backend-mqtt-db-agent' pod is in '**Running**' state -

		kubectl get pods

	> **Note:** You may check the Pod **Logs** using the command '**kubectl logs \<pod_name\>**'		

## 3. Deploy REST API Agent:

The 'REST API Agent' would act as the gateway to the backend application. It will listen to the incomming HTTP requests from the frontend application that you will deploy on Google Cloud.

### 3.1 Deploy REST API Agent:
* **3.1.1: Deploy REST API Agent -** Use the following command to create the rest-api-agent kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent.yaml

* **3.1.2: Check Deployment Status -** Use the following command to check if the kubernetes deployment was created successfully or not -

		kubectl get deployment iot-backend-rest-api-agent
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_agent.png)
	
* **3.1.3: Check Pod Status -** Use the following command to check if the 'iot-backend-rest-api-agent' pod is in '**Running**' state -

		kubectl get pods

	> **Note:** You may check the Pod **Logs** using the command '**kubectl logs \<pod_name\>**'	


### 3.2 Expose REST API Agent to Google Cloud using Kubernetes Service:

Since the frontend app from Google Cloud would access the REST APIs exposed by the 'REST API Agent', you need to create a new kubernetes service for it.

* **3.2.1: Create REST API Agent NodePort Service -** You can create a new kubernetes service using the following command -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent_service_node_port.yaml

* **3.2.2: Check REST API Agent Service Status -** You can use the following command to check if the kubernetes service was creted successfully or not -

		kubectl get service rest-api-agent-service
		
	You should have the output similar to the following screenshot -
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_agent_service.png)
	
### 3.3 Locate the IP and Port to Access Node-Port Service:

You need to find the NodePort and Kubernetes Node external IP to access the 'rest-api-agent.

* Use the following command to display the port exposed by 'rest-api-agent-service' -

		kubectl get service rest-api-agent-service

* Use the following command to display the 'External-IP' of you kubernetes nodes -

		kubectl get nodes -o wide

	Following screenshot highlights the Port and Node IPs in the command outputs -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/node_port_service.png)

>**Important:** Note down the Node External IP Address and NodePort Service Port Number. These values would be used in next section for deploying the frontend app as the environment variables values ('**BACKEND\_HOST**' and '**BACKEND\_PORT**').

## 4 Test the REST API Agent Service:

To test the REST API service try to access following url from your web browser (use the node's external ip and service port from the previous section # 3.3)-

	http://<node's external ip>:30500/
	
If your REST API Agent is working properly, you should see 'Welcome to the API Service...!' message on your browser as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_url_test.png)

Following are the other urls that you could test -

	http://<node's external ip>:30500/cities
	
	http://<node's external ip>:30500/temperature
	
	http://<node's external ip>:30500/humidity
	
	http://<node's external ip>:30500/sensor_data/city
	
## Next Steps:

You have successfully deployed all the backend components of the iot-app on the CCP kubernetes cluster. Now you may proceed futher and deploy the frontend components on Google Cloud.






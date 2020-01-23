# Deploy the Backend Application Components on CCP Kubernetes Cluster (CCP Tenant Cluster)


In this section you would deploy the backend components of the IoT Application on the Kubernetes cluster deployed on your CCP instance. Following diagram shows the high-level architecture of these backend application containers

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/backend_app_architecture.png)

## Login to Kubernetes Master CLI Shell:

SSH into Linux Jumphost using Putty (172.18.0.50) - use your credentials. From here you will deploy two microservices in on-premise Kubernetes Cluster and one microservice in AWS EKS Kubernetes cluster. You will see how microservices talks to each other and how to establish necessary communication.

## 1. Deploy MariaDB Databse:

MariaDB will be used in the backend to save the sensor data received from AWS IoT platform over MQTT protocol. For this we would create following objects -

1. Kubernetes Secret
2. Kubernetes Persistent Volume Claim (PVC)
3. Kubernetes MariaDB Deployment
4. Kubernetes ClusterIP Service (Headless Service)

Following diagram shows the relationship between these objects -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb_kubernetes_deployment.png)

### 1.1 Create Kubernetes Secret for MariaDB:

A **Kubernetes Secret** is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in an image; putting it in a Secret object allows for more control over how it is used, and reduces the risk of accidental exposure.

The MariaDB container image uses an environment variable named as 'MYSQL\_ROOT\_PASSWORD', it hold the root password required to access the database. So you would create a new secret with 'password' key (value as 'cisco123') which would later be used in mariaDB deployment yaml file.

* **1.1.1: Switch context to on-premise Kubernetes Cluster -** Change context of `kubectl` command to access on-premise Kubernetes Cluster.

		kubectl config use-context on-prem-1
		kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-use-on-prem.png">

* **1.1.2: Create DB Password Secret -** Use the following command to create a new secret on your kubernetes cluster -

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **1.1.3: Verify DB Password Secret -** Check if the secret was created successfully or not -

		kubectl get secret mariadb-root-pass
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb-secret-onprem.png)
	

### 1.2 Create Kubernetes Persistent Volume Claim for MariaDB:

A **Kubernetes Persistent Volume Claim (PVC)** is a request for storage by a user. It is similar to a pod. Pods consume node resources and PVCs consume Persistent Volume (PV) resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., can be mounted once read/write or many times read-only).

To keep the sensor data safe during Pod restarts, you would create a new Persistent Volume Claim. 

The following yaml definition would be used to create the 'PersistentVolumeClaim' - 

```yaml
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
```
* **1.2.1: Create Persistent Volume Claim -** Use the following command to create a new Persistent Volume Claim for MariaDB Pod -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_persistent_volume.yaml

* **1.2.2: Verify Persistent Volume Claim -** Check if the PVC was created successfully or not -

		kubectl get pvc mariadb-pv-claim
	
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/pvc-on-prem.png)
	
>**Important:** It can take up to a few minutes for the PVs to be provisioned. DO NOT procced futher till the PVC deployment gets completed.
	
### 1.3 Deploy MariaDB on Kubernetes:

**MariaDB** is a community-developed fork of the MySQL relational database management system intended to remain free under the GNU GPL. Development is led by some of the original developers of MySQL, who forked it due to concerns over its acquisition by Oracle Corporation. MariaDB intends to maintain high compatibility with MySQL, ensuring a drop-in replacement capability with library binary parity and exact matching with MySQL APIs and commands.

The following yaml definition will be used to deploy MariaDB pod -

```yaml
---
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: iot-backend-mariadb
  labels:
    app: iot-backend
spec:
  selector:
    matchLabels:
      app: iot-backend
      tier: mariadb
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: iot-backend
        tier: mariadb
    spec:
      containers:
      - image: mariadb:10.3
        name: mariadb
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mariadb-root-pass
              key: password
        ports:
        - containerPort: 3306
          name: mariadb
        volumeMounts:
        - name: mariadb-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mariadb-persistent-storage
        persistentVolumeClaim:
          claimName: mariadb-pv-claim
```
* **1.3.1: Deploy MariaDB -** Use the following command to create a MariaDB kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_deployment.yaml
		
* **1.3.1: Check Deployment Status -** Use the following command to check if the kubernetes deployment was successfully created or not -

		kubectl get deployment iot-backend-mariadb
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb-deployment-status.png)
	
* **1.3.2: Check Pod Status -** Use the following command to check if the 'iot-backend-mariadb' pod is in '**Running**' state -

		kubectl get pods

> **Note:** Kubernetes may take some time to deploy the MariaDB. **DO NOT** proceed further till the time DB Pod is up.	
		
### 1.4 Create Kubernetes LoadBalancer Service for MariaDB:

Since the MariaDB will be accessed by other services like 'MQTT to DB Agent' and 'REST API Agent'; you need to expose it externally, since 'MQTT to DB Agent' will be running on another Kubernetes Cluster

A **Kubernetes LoadBalancer Service** is provides external access to your application from systems outside of Kubernetes. LoadBalancer service is exposed under dedicated VIP address, routable in external network. Traffic directed to this IP address is load balanced by Kubernetes across Kubernetes nodes.

Following yaml definition would be used to create the LoadBalancer Service for MariaDB -

```yaml
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
  selector:
    app: iot-backend
    tier: mariadb
  type: "LoadBalancer"
```

* **1.4.1: Expose MariaDB to other Pods -** Create a new kubernetes service using the following command -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Mariadb/mariadb_service.yaml
				
* **1.4.2: Verify Service Status -** Use the following command to check if the kubernetes service was deployed successfully or not -

		kubectl get service mariadb-service
		
	You should have the output similar to the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb-service-lb.png)

## 2. Deploy REST API Agent on Kubernetes:

The 'REST API Agent' would act as the gateway to the backend application. It will listen to the incoming HTTP requests from the frontend application that you will deploy on Google Cloud.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_agent_deployment.png)

### 2.1 Deploy REST API Agent:

The following yaml definition will be used to create REST API Agent pods -

```yaml
---
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: iot-backend-rest-api-agent
  labels:
    app: iot-backend-rest-api-agent
spec:
  replicas: 1
  selector:
    matchLabels:
      app: iot-backend-rest-api-agent
      tier: rest-api-agent
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: iot-backend-rest-api-agent
        tier: rest-api-agent
    spec:
      containers:
      - image: pradeesi/rest_api_agent:v1
        name: rest-api-agent
        env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mariadb-root-pass
              key: password
```

* **2.1.1: Deploy REST API Agent -** Use the following command to create the rest-api-agent kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent.yaml

* **2.1.2: Check Deployment Status -** Use the following command to check if the kubernetes deployment was created successfully or not -

		kubectl get deployment iot-backend-rest-api-agent
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/restapi-deployment.png)
	
* **2.1.3: Check Pod Status -** Use the following command to check if the 'iot-backend-rest-api-agent' pod is in '**Running**' state -

		kubectl get pods

	> **Note:** You may check the Pod **Logs** using the command '**kubectl logs \<pod_name\>**'	


### 2.2 Create Kubernetes NodePort Service for REST API Agent:

Since the frontend app from Google Cloud would access the REST APIs exposed by the 'REST API Agent', you need to create a new kubernetes service for it.

The following yaml definition would be used for to create a NodePort Service for the REST API Agent -

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: rest-api-agent-service
  labels:
    app: iot-backend
spec:
  ports:
    - protocol: TCP
      port: 5050
  selector:
    app: iot-backend-rest-api-agent
    tier: rest-api-agent
  type: "NodePort"
```

* **2.2.1: Create REST API Agent NodePort Service -** You can create a new kubernetes service using the following command -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/REST_API_Agent/rest_api_agent_service_node_port.yaml

* **2.2.2: Check REST API Agent Service Status -** You can use the following command to check if the kubernetes service was created successfully or not -

		kubectl get service rest-api-agent-service
		
	You should have the output similar to the following screenshot -
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/restapi-service.png)
	
### 2.3 Locate the IP and Port to Access Node-Port Service for REST API Agent:

You need to find the NodePort and Kubernetes Node external IP to access the 'rest-api-agent.

* Use the following command to display the port exposed by 'rest-api-agent-service' -

		kubectl get service rest-api-agent-service

* Use the following command to display the 'External-IP' of you kubernetes nodes -

		kubectl get nodes -o wide

	Following screenshot highlights the Port and Node IPs in the command outputs -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/restapi-service-ip.png)

>**Important:** Note down the Node External IP Address and NodePort Service Port Number. These values would be used in next section for deploying the frontend app as the environment variables values ('**BACKEND\_HOST**' and '**BACKEND\_PORT**').

## 3. Deploy MQTT to DB Agent on Kubernetes:

'MQTT to DB Agent' will subscribe to the MQTT Topic and listen to the incoming sensor data from AWS IoT platform. It will then parse the sensor data and insert it into the MariaDB.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mqtt_db_agent_deployment.png)

The following yaml definition will be used to create the MQTT to DB Agent pods -

```yaml
---
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: iot-backend-mqtt-db-agent
  labels:
    app: iot-backend
    tier: mqtt-db-agent
spec:
  selector:
    matchLabels:
      app: iot-backend-mqtt-db-agent
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: iot-backend-mqtt-db-agent
    spec:
      containers:
      - image: pradeesi/mqtt_db_plugin:v2
        name: mqtt-db-agent
        env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mariadb-root-pass
              key: password
```
* **3.1: Switch context to AWS EKS Kubernetes Cluster -** Change context of `kubectl` command to access on-premise Kubernetes Cluster.

		kubectl config use-context aws
		kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-use-aws.png">

* **3.2: Create DB Password Secret -** Use the following command to create a new secret on your kubernetes cluster -

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **3.3: Verify DB Password Secret -** Check if the secret was created successfully or not -

		kubectl get secret mariadb-root-pass
		
	You should have the output similar to the following screenshot -
	
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb-secret-onprem.png)
	
* **3.4: Create external service -** MQTT needs to send data to database that is deployed in different Kubernetes Cluster. MQTT application is configured to contact with MariaDB using following internal DNS name: `mariadb-service`. We need to configure Kubernetes to resolve this name to a particular LoadBalancer IP that has been allocated to your `mariadb-service` in on-premise Kubernetes Cluster. For this we will define service and manually add endpoint that this service will resolve to. In the Endpoint definition you have to specify your LoadBalancer IP address from on-premise Kubernetes Cluster allocated to `mariadb-service`.

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: mariadb-service
spec:
  ports:
    - name: sql
      protocol: TCP
      port: 3306
      targetPort: 3306
---
apiVersion: v1
kind: Endpoints
metadata:
name: mariadb-service
subsets:
- addresses:
  - ip: LoadBalancerIP ## Specify mariadb-service LoadBalancer IP from step 1.4
    ports:
    - port: 3306
      name: sql
```
Download following definition file:

	wget https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/MQTT_DB_Agent/mariadb-ext-service-eks.yaml

Check string to be replaced by LoadBalancerIP allocated to mariadb-service from Step 1.4.2

```bash
	cat mariadb-ext-service-eks.yaml
```
<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/cat-mariadb-template.png">

Change `<mariadb-service_LoadBalancer_IP>` with IP address of your load balancer IP.

```bash
	cat mariadb-ext-service-eks.yaml
	sed -i 's/<mariadb-service_LoadBalancer_IP>/172.18.0.XXX/g' mariadb-ext-service-eks.yaml  ## replace 172.18.0.XXX with the IP address of LoadBalancer IP allocated to mariadb-service in on-premise Kubernetes Cluster.
```

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mariadb-change-ip.png">

> IMPORTANT! Make sure the address you specified is correct !

Apply updated manifest to create external service access:

	kubectl apply -f mariadb-ext-service-eks.yaml

Check services and associated endpoints:

	kubectl get svc,endpoints

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/eks-get-svc-endpoints.png">

* **3.5: Deploy MQTT to DB Agent -** Use the following command to create mqtt-to-db-agent kubernetes deployment -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/MQTT_DB_Agent/mqtt_db_agent_deployment.yaml


* **3.6: Check Deployment Status -** Use the following command to check if the kubernetes deployment was created successfully or not -

		kubectl get deployment iot-backend-mqtt-db-agent
		
	You should have the output similar to the following screenshot -
		
	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/mqtt-deployment.png)
	
* **3.5: Check Pod Status -** Use the following command to check if the 'iot-backend-mqtt-db-agent' pod is in '**Running**' state -

		kubectl get pods	

## 4 Test the REST APIs Exposed by REST API Agent Service:

To test the REST API service try to access following url from your web browser (use the node's external ip and service port from the previous section # 2.3) -
If you haven't note the IP and port information earlier, please follow these steps - 

Change `kubectl` context to `on-prem-1`

    kubectl config use-context on-prem-1
    kubectl config get-contexts

> Make sure stat is no in front of `on-prem-1` Kubernetes Cluster.

* Use the following command to display the port exposed by 'rest-api-agent-service' -

		kubectl get service rest-api-agent-service

* Use the following command to display the 'External-IP' of you kubernetes nodes -

		kubectl get nodes -o wide

	Following screenshot highlights the Port and Node IPs in the command outputs -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/restapi-service-ip.png)
	
Now you have open Chrome browser and specify URL based on pattern - 

	http://<kubernetes node's external ip>:<nodePort>
  i.e. http://172.18.0.169:30423

If your REST API Agent is working properly, you should see 'Welcome to the API Service...!' message on your browser as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rest_api_url_test.png)

Following are the other urls that you could test -

	http://<kubernetes node's external ip>:<nodePort>/cities
	
	http://<kubernetes node's external ip>:<nodePort>/temperature
	
	http://<kubernetes node's external ip>:<nodePort>/humidity
	
	http://<kubernetes node's external ip>:<nodePort>/sensor_data/city
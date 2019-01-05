# Deploy Frontend Application

## Objective:

In this section we would deploy the 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/frontend_app_architecture.png)



## Login to Google Cloud Console and Open Kubernetes Engine:

Login to Google Cloud Console using the credentials provided by the lab instructor.

## Deploy Frontend App

### 1. Start Creating Deployment Definition:

* **1.1:** Select the '**Workloads**' option on "**Google Cloud Console --> Kubernetes Engine**" page, and click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_1.png)

### 2. Add 'frontend_server' Container Image to the Deployment Definition:

* **2.1:** Click on the '**Select Google Container Registry Image**' button on the 'Create Deployment' page as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_2.png)

* **2.2:** Select the '**frontend_server**' container image from the pop-up window and clikc on the '**SELECT**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_3.png)

### 3. Add Environment Variables to the 'frontend_server' Container:

* **3.1:** Click on the '+ Add environment variable' button to add the environment variables for the 'frontend_server' container as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_4.png)

* 3.2: Add 'BACKEND_HOST' and 'BACKEND_PORT' variables as shown in the following screenshot -
 
 > **Important:** Use the values IP and Port values from the backend REST API Service.

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_5.png)

### 4. Add Second Container Image ('nginx_srvr') to the Deployment Definition:

* **4.1:** 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_6.png)

### 5. Add Application Name, Select Cluster and Deploy the Application:

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_7.png)

### 6. Expose the Application by Creating Kubernetes Service: 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_8.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_9.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_10.png)

### 7. Open the Application Dashboard:

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_11.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_12.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_14.png)



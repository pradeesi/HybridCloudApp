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

* **3.2:** Add '**BACKEND\_HOST**' and '**BACKEND\_PORT**' variables as shown in the following screenshot -
 
 > **Important:** Use the values for 'BACKEND\_HOST' and 'BACKEND\_PORT' from the REST API Agent **NodePort Service**.

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_5.png)

### 4. Add Second Container Image ('nginx_srvr') to the Deployment Definition:

* **4.1:** After clicking on the '**+ Add Container**' button (shown in the previous screenshot), click again on the '**Select Google Container Registry image**' and select '**nginx_srvr**' image from the pop-up window. 

	After selecting the image, click on the '**Done**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_6.png)

### 5. Add Application Name, Select Cluster and Deploy the Application:

* **5.1:** Verify that you have '**frontend_server**' and '**nginx_srvr**' container images selected on your screen.

* **5.2:** Change the application name to '**iot-frontend-\<user-\#\>**' and select the 'Cluster' from the drop down menu. 

	Now you can click on the 'Deploy' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_7.png)
	
	> **Importnat:** Application deployment may take some time. Wait for it's completion before proceeding with the next steps.

### 6. Expose the Application by Creating Kubernetes Service:

* **6.1:** Click on your Workload 'Name' (Deployment) as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_8.png)

* **6.2:** Click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_9.png)
	
* **6.3:** In the 'New Port Mapping' set '**Port**' and '**Target Port**' as '**80**' and click on the '**Done**' button.

	Make sure the '**Service type**' is '**Load balancer**' and click on the '**Expose**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_10.png)
	
	> **Important:** Service deployment may take some time. Wait for it before proceeding with the next steps.

### 7. Open the Application Dashboard:

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_11.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_12.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_14.png)



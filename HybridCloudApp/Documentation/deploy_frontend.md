# Deploy the Frontend Application Components on Google Kubernetes Engine (GKE)

In this section you would deploy the frontend components of the IoT Application on the Google Kubernetes Engine. Following diagram shows the high-level architure of these frontend application containers -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/frontend_app_architecture.png)


### 1. Login to Google Cloud Console and Open Kubernetes Engine:

* Login to Google Cloud Console using the credentials provided by the lab instructor.


### 2. Start Creating Deployment Definition:

* **2.1:** Select the '**Workloads**' option on "**Google Cloud Console --> Kubernetes Engine**" page, and click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_1.png)

### 3. Add 'frontend_server' Container Image to the Deployment Definition:

* **3.1:** Click on the '**Select Google Container Registry Image**' button on the 'Create Deployment' page as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_2.png)

* **3.2:** Select the '**frontend_server**' container image from the pop-up window and clikc on the '**SELECT**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_3.png)

### 4. Add Environment Variables to the 'frontend_server' Container:

* **4.1:** Click on the '+ Add environment variable' button to add the environment variables for the 'frontend_server' container as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_4.png)

* **4.2:** Add '**BACKEND\_HOST**' and '**BACKEND\_PORT**' variables as shown in the following screenshot -
 
 > **Important:** Use the values for 'BACKEND\_HOST' and 'BACKEND\_PORT' from the REST API Agent **NodePort Service**.
 

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_5.png)

### 5. Add Second Container Image ('nginx_srvr') to the Deployment Definition:

* **5.1:** After clicking on the '**+ Add Container**' button (shown in the previous screenshot), click again on the '**Select Google Container Registry image**' and select '**nginx_srvr**' image from the pop-up window. 

	After selecting the image, click on the '**Done**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_6.png)

### 6. Add Application Name, Select Cluster and Deploy the Application:

* **6.1:** Verify that you have '**frontend_server**' and '**nginx_srvr**' container images selected on your screen.

* **6.2:** Change the application name to '**iot-frontend-\<user-\#\>**' and select the 'Cluster' from the drop down menu. 

	Now you can click on the 'Deploy' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_7.png)
	
	> **Importnat:** Application deployment may take some time. Wait for it's completion before proceeding with the next steps.

### 7. Expose the Application by Creating Kubernetes Service:

* **7.1:** Click on your Workload 'Name' (Deployment) as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_8.png)

* **7.2:** Click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_9.png)
	
* **7.3:** In the 'New Port Mapping' set '**Port**' and '**Target Port**' as '**80**' and click on the '**Done**' button.

	Make sure the '**Service type**' is '**Load balancer**' and click on the '**Expose**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_10.png)
	
	> **Important:** Service deployment may take some time. Wait for it before proceeding with the next steps.

### 8. Open the Application Dashboard:

* **8.1:** Go to '**Kubernetes Engine --> Services**' and cick on the '**Endpoints**' respective to your kubernetes service as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_11.png)

* **8.2:** You should see the following webpage in the new tab of your browser. Click on the "Open Dashboard" button to open the application dashboard as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_12.png)
	
* **8.3:** If you see the following web-page with charts filled with data, your application is working :-) Congratulations!!!

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_14.png)



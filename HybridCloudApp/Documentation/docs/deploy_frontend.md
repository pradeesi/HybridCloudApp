# Deploy the Frontend Application Components on Google Kubernetes Engine (GKE)

In this section you would deploy the frontend components of the IoT Application on the Google Kubernetes Engine. Following diagram shows the high-level architecture of these frontend application containers -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/frontend_app_architecture.png)


### 1. Login to Google Cloud Console and Open Kubernetes Engine:

Login to Google Cloud Console using the credentials from credentials page.

You can find the details of login method at this link - [Google Cloud Access](/LAB_access/#5-google-cloud-access)

### 2. Creating Deployment Definition using GKE UI on Google Cloud Console:

You will create kubernetes deployment for frontend app and expose it to the internet using Kubernetes Load Balancer Service as shown in the following diagram -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_frontend_srvr.png)

* **2.1:** Select the '**Workloads**' option on "**Google Cloud Console --> Kubernetes Engine**" page, and click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_1.png)

### 3. Add 'frontend_server' Container Image to the Deployment Definition:

* **3.1:** Select the '**Existing container image**' radio button on the 'Create Deployment' page and then click on 'SELECT' button to select the image as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/select_container1.png)

* **3.2:** Select the '**frontend_server**' container image from the pop-up window and click on the '**SELECT**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/select_frontend_srvr_image1.png)

### 4. Add Environment Variables to the 'frontend_server' Container:

* **4.1:** Click on the '+ Add environment variable' button to add the environment variables for the 'frontend_server' container as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/add_environment_1.png)

* **4.2:** Add '**BACKEND\_HOST**' and '**BACKEND\_PORT**' variables as shown in the following screenshot (Use the values for 'BACKEND\_HOST' and 'BACKEND\_PORT' from the REST API Agent **NodePort Service** created earlier) -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/add_env_variable2.png)

### 5. Add Second Container Image ('nginx_srvr') to the Deployment Definition:

* **5.1:** After clicking on the '**+ Add Container**' button (shown in the previous screenshot), click again on the '**Existing ontainer image**' and click on the '**SELECT**' button. It will display the popup window. For this popup window, select the '**nginx_srvr**' image with 'latest' tag.

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/select_nginx_image2.png)

* **5.2:** Click on the 'CONTINUE' button as shown in the following screenshot -


	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/continue2.png)



### 6. Add Application Name, Select Cluster and Deploy the Application:


* **6.1:** Change the application name to '**iot-frontend-user-X**' (Replace X with you POD number) and select the 'Cluster' from the drop down menu.

	Now you can click on the 'Deploy' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy1.png)
	
	> **Importnat:** Application deployment may take some time. Wait for it's completion before proceeding with the next steps.

### 7. Expose the Application by Creating Kubernetes Service:

Click on '**Workloads**' option from the left panel on the GKE Dashboard.

* **7.1:** Click on your Workload name '**iot-frontend-user-X**' (Kubernetes Deployment) as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_8.png)

* **7.2:** Click on the '**Deploy**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_9.png)
	
* **7.3:** In the 'New Port Mapping' set '**Port**' and '**Target Port**' as '**80**' and click on the '**Done**' button.

	Make sure the '**Service type**' is '**Load balancer**' and click on the '**Expose**' button as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_10.png)
	
	> **Important:** Service deployment may take some time. Wait for it before proceeding with the next steps.

### 8. Open the Application Dashboard:

* **8.1:** Go to '**Kubernetes Engine --> Services**' and click on the '**Endpoints**' respective to your kubernetes service as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_11.png)

* **8.2:** You should see the following webpage in the new tab of your browser. Click on the "Open Dashboard" button to open the application dashboard as shown in the following screenshot -

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_12.png)
	
* **8.3:** If you see the following web-page with charts filled with data, your application is working :-) Congratulations!!!

	![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_14.png)



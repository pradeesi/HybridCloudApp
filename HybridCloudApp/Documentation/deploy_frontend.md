# Deploy Frontend Application

## Objective:

In this section we would deploy the 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/frontend_app_architecture.png)



## Login to Google Cloud Console and Open Kubernetes Engine:

Login to Google Cloud Console using the credentials provided by the lab instructor.

## Deploy Frontend App

### 1. Select the 'Workloads' Option and Start the Deployment

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_1.png)

### 2. Add 'frontend_server' Container Image to the Deployment Definition:

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_2.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_3.png)

### 3. Add Environment Variables to the 'frontend_server' Container:

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_4.png)

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/deploy_gke_workload_5.png)

### 4. Add Second Container Image ('nginx_srvr') to the Deployment Definition:

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



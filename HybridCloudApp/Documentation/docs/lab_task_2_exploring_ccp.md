# Lab Task 2: Exploring Cisco Container Platform



Cisco Container Platform is a production grade platform to manage, monitor and deploy Kubernetes Clusters in your Enterprise. 
CCP uses 100% upstream Kuberenetes without vendor specific modification creating seamless experience for developer to deploy application in any kubernetes platform in the cloud or on-premise in private cloud.  
Cisco Container Platform has two main architecture components:
- Control Plane Cluster - to provide management platform for your Kubernetes Clusters where you can deploy new, scale worker nodes, manage policy and networking. The Control Plane is also build based on Kubernetes.
- Tenant Cluster - the Kubernetes cluster used to host applications across production, development, staging and many other environments

Each user in this lab will have his own Cisco Container Platform Control Plane.  
As described in the Lab task 1, check Table 1 with the URL to access your CCP Control Plane cluster dashboard.

## 1. Explore CCP dashboard

Login to CCP Dashboard - find URL in [Table 1](../lab_task_1_environment_access.md), use your Active Directory credentials that you can find in *credentials.txt* file. 

Once logged in, you will be taken to the "cluster" page.
In this page you can manage your kubernetes clusters, edit their configuration, adding nodes or create node policies.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty.png">

In the left pane you will see other options such as `User management`, where users or group of users are managed locally or authentication could be integrated with Active Directory services. In our lab, Cisco Container Platform has been integrated with Active Directory.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-user-mgmt-ad.png">

In the next menu position, you will see `Infrastructure Providers`. This is place where you select your cloud infrastructure, either it could be on-prem vmware vSphere or public cloud - Amazon Web Services.  Cisco Container Platform requests resources such as virtual machines that later on will act as master and worker nodes of your Kubernetes cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-infra-providers-vmware.png">

`Networks` provides IP addressing subnets and pools configuration for the tenant clusters. When tenant cluster is deployed, the IP addresses for nodes are allocated from DHCP, however, Cisco Container Platform provides built-in mechanism to allocate IP addresses for Service under which applications will be exposed externally. This mechanism is explaining later in the lab 3 **add reference to lab with VIP pools**

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-networks-main.png">

The last tab contains `Licensing`, where you can register your Cisco Container Platform with Smart Licensing server.


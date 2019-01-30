# Exploring Cisco Container Platform


Cisco Container Platform is a production grade platform to manage, monitor and deploy Kubernetes Clusters in your Enterprise. 
CCP uses 100% upstream Kuberenetes without vendor specific modification, creating seamless experience for developer to deploy application on any kubernetes platform in the public or private cloud.  

CCP provides authentication and authorization, security, high availability, networking, load balancing, and operational capabilities to effectively operate and manage Kubernetes clusters. CCP also provides a validated configuration of Kubernetes and can integrate with underlying infrastructure components such as Cisco HyperFlex and Cisco ACI. The infrastructure provider for CCP is Hyperflex.

Cisco Container Platform has two main architecture components:
* Control Plane Cluster - to provide management platform for your Kubernetes Clusters where you can deploy new, scale worker nodes, manage policy and networking. The Control Plane is also build based on Kubernetes.
* Tenant Data Cluster - the Kubernetes cluster used to host applications across production, development, staging and many other environments

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp_features.png">

Each user in this lab will have own Cisco Container Platform Control Plane.  
As described in the Lab task 1, check Table 1 with the URL to access your CCP Control Plane cluster dashboard.

## Explore CCP dashboard

Login to your dedicated CCP Dashboard - find URL in [Table 1](#3-accessing-vcenter), use your Active Directory credentials that you can find in paper sheet on your desk.

Once logged in, you will be taken to the "cluster" page.
In this page you can manage your kubernetes clusters, edit their configuration, adding nodes or create node policies.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty-no_marks.png">

In the left pane you will see other options such as `User management`, where users or group of users are managed locally or authentication could be integrated with Active Directory services. In our lab, Cisco Container Platform has been integrated with Active Directory.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-user-mgmt-ad.png">

In the next menu position, you will see `Infrastructure Providers`. This is place where you select your cloud infrastructure, either it could be on-prem VMware vSphere or public cloud - Amazon Web Services.  Cisco Container Platform requests resources such as virtual machines that later on will act as master and worker nodes of your Kubernetes cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-infra-providers-vmware.png">

`Networks` provides IP addressing subnets and pools configuration for the tenant clusters. When tenant cluster is deployed, the IP addresses for nodes are allocated from DHCP, however, Cisco Container Platform provides built-in mechanism to allocate IP addresses for Service Expousure under which applications will be exposed externally. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-networks-main.png">

The last tab contains `Licensing`, where you can register your Cisco Container Platform with Smart Licensing server.


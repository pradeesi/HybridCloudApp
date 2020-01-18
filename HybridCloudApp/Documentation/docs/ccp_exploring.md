# Exploring Cisco Container Platform


Cisco Container Platform is a production grade platform to manage, monitor and deploy Kubernetes Clusters in your Enterprise. 
CCP uses 100% upstream Kuberenetes without vendor specific modification, creating seamless experience for developer to deploy application on any kubernetes platform in public or private cloud.  

CCP provides authentication and authorization, security, high availability, networking, load balancing, and operational capabilities to effectively operate and manage Kubernetes clusters. CCP also provides a validated configuration of Kubernetes and can integrate with underlying infrastructure components such as Cisco HyperFlex and Cisco ACI.

Cisco Container Platform has two main architecture components:
* Control Plane Cluster - to provide management platform for your Kubernetes Clusters where you can deploy new production grade Kubernetes Clusters, scale worker nodes, manage policy and networking. The Control Plane is also build based on Kubernetes.
* Tenant Cluster - the Kubernetes cluster used to host applications across production, development, staging and many other environments

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-components.png">

Each user in this lab will have own Cisco Container Platform Control Plane.  
As described in the Lab task 1, check Table 1 with the URL to access your CCP Control Plane cluster dashboard.

## Explore CCP dashboard

Login to your dedicated CCP Dashboard - find URL and credentials that you can find in paper sheet on your desk.

Once logged in, you will be taken to the "cluster" page.
In this page you can manage your kubernetes clusters across multiple infrastructure providers, edit their configuration, adding nodes or create node policies.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-ui.png">

In the next menu position, you will see `Infrastructure Providers`. This is place where you configure to access your cloud infrastructure Provider, either it could be on-premise VMware vSphere (vCenter access) 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-infra-provider-vmware.png">

or public cloud - Amazon Web Services or Azure. Cisco Container Platform leverage one of these profiles to deploy Tenant Clusters in specific Infrastructure Provider.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-aws-provider.png">

`Networks` provides IP addressing subnets and pools configuration for the tenant clusters on-premise (vSpehre). When tenant cluster is deployed, you can manage pool of IP addresses available to allocate for LoadBalancer under which applications will be exposed externally.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-network-pools.png">

Cisco Container Platform provides out-of-the-box ACI integration with Tenant Clusters. During installation of Cisco Container Platform Control Plane (the platform that provides GUI that you are now browsing through), you can select Kubernetes CNI solution. CCP supports Calico (the one used in this lab), Cisco ACI CNI or high performance Contiv-VPP CNI.
For Cisco ACI-CNI, new tenant clusters are deployed with ACI integration. No need later to configure it separately.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-networks-main.png">

`User Management` provides panel to manage authentication providers, users, groups and policies. Users can be authenticated against local database or from Active Directory. Authorization policy allocates user to particular Tenant Cluster, You can allocate access for the developer team to manage only their own Kubernetes cluster (expand number of nodes, manage IP addresses pool available for Load Balancing services).

The last tab provides `Licensing` settings, where you can register your Cisco Container Platform with Smart Licensing server.


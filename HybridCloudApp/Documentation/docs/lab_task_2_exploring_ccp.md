# Lab Task 2: Exploring Cisco Container Platform



Cisco Container Platform is a production grade platform to manage, monitor and deploy Kubernetes Clusters in your Enterprise. 
CCP uses 100% upstream Kuberenetes without vendor specific modification creating seamless experience for developer to deploy application in any kubernetes platform in the cloud or on-premise in private cloud.  
Cisco Container Platform has two main architecture components:
- Control Plane Cluster - to provide management platform for your Kubernetes Clusters where you can deploy new, scale worker nodes, manage policy and networking. The Control Plane is also build based on Kubernetes.
- Tenant Cluster - the Kubernetes cluster used to host applications across production, development, staging and many other environments

Each user in this lab will have his own Cisco Container Platform Control Plane.  
As described in the Lab task 1, check Table 1 with the URL to access your CCP Control Plane cluster dashboard.

## 1. Create tenant cluster in CCP

Login to CCP Dashboard - find URL in [Table 1](../lab_task_1_environment_access.md), user your Active Directory credentials that you can find in *credentials.txt* file. 


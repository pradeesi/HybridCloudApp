# Connect AWS EKS Kubernetes Cluster to Hybrid Network

After successfully created EKS cluster, now it is a time to connect it to VPN connection towards On-Premise Data Center.
CCP created dedicated VPC for every Kubernetes EKS Cluster. You can now start working on it and deploying applicaitons, however your services and applications will be exposed to public Internet. In our scenario, we will be deploying backend part of our application in EKS cluster that needs to have connectivity to database that you will deploy on-premise.

In order to provider secure connectivity between application components, we would need to establish IPSec Tunnel between AWS and on-premise data center. To avoid too many IPsec tunnels, we will leverage following topology, where AWS VPC infrastructure is configured in Hub-and-Spoke topology with Transit VPC as a Hub location. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-transit.png">
# Connect AWS EKS Kubernetes Cluster to Hybrid Network

After successfully created EKS cluster, now it is a time to connect it to VPN connection towards On-Premise Data Center.
CCP created dedicated VPC for every Kubernetes EKS Cluster. You can now start working on it and deploying applicaitons, however your services and applications will be exposed to public Internet. In our scenario, we will be deploying backend part of our application in EKS cluster that needs to have connectivity to database that you will deploy on-premise.

In order to provider secure connectivity between application components, we would need to establish IPSec Tunnel between AWS and on-premise data center. To avoid too many IPsec tunnels, we will leverage following topology, where AWS VPC infrastructure is configured in Hub-and-Spoke topology with Transit VPC as a Hub location. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-transit.png">

This solution is well described in two following white papers:

[https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/architecture.html](https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/architecture.html)

In this topology we have Transit VPC with 2x CSR1000v virtual routers deployed in AWS account. Those routers have already configured IPSec Tunnel to On-Premise with BGP routing protocol. All you need to do now is to attach this VPC as a spoke. Subnets from your new VPC will be advertised to CSR1000v in transit VPC and then further to On-Premise Data Center.
Solution automate VPN Gateway discovery and creates VPN site-to-site connection to transit VPC CSR1000v. In your new VPC you have to attach AWS VPN Gateway, and assign specific tag to it. Serverless Lamba component runs a script every minute to look for new VPC's with that particulat TAG. When it is found, another script is invoked to create IPSec configuration on CSR1000v in Transit VPC towards VPN Gateway.

## Create AWS VPN Gateway 

Open AWS dashboard, and select VPC service, as on the following picture:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-transit.png">


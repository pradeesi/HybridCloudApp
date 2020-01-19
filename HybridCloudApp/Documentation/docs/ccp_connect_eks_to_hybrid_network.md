# Connect AWS EKS Kubernetes Cluster to Hybrid Network

After successfully created EKS cluster, now it is a time to connect it to VPN connection towards On-Premise Data Center.
CCP created dedicated VPC for every Kubernetes EKS Cluster. You can now start working on it and deploying applicaitons, however your services and applications will be exposed to public Internet. In our scenario, we will be deploying backend part of our application in EKS cluster that needs to have connectivity to database that you will deploy on-premise.

In order to provider secure connectivity between application components, we would need to establish IPSec Tunnel between AWS and on-premise data center. To avoid too many IPsec tunnels, we will leverage following topology, where AWS VPC infrastructure is configured in Hub-and-Spoke topology with Transit VPC as a Hub location. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-transit-vpc-architecture.png">

This solution is well described in two following white papers:

[https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/architecture.html](https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/architecture.html)

In this topology we have Transit VPC with 2x CSR1000v virtual routers deployed in AWS account. Those routers have already configured IPSec Tunnel to On-Premise with BGP routing protocol. All you need to do now is to attach this VPC as a spoke. Subnets from your new VPC will be advertised to CSR1000v in transit VPC and then further to On-Premise Data Center.
Solution automate VPN Gateway discovery and creates VPN site-to-site connection to transit VPC CSR1000v. In your new VPC you have to attach AWS VPN Gateway, and assign specific tag to it. Serverless Lamba component runs a script every minute to look for new VPC's with that particulat TAG. When it is found, another script is invoked to create IPSec configuration on CSR1000v in Transit VPC towards VPN Gateway.

## Create AWS VPN Gateway 

- **Step 1.** Open AWS dashboard, and select VPC service, as on the following picture:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-enter.png">

Next make sure your VPC has been created with your username in front of the name.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-find.png">

- **Step 2.** Select Virtual Private Gateways from the left menu.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-vgw-enter.png">

- **Step 3.** Create Virtual Private Gateway

Press button *Create Virtual Private Gateway*

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-create.png">

Enter your username as a name of Virtual Private Gateway (studentXX) and leave *default ASN* selected (autonomous system number for BGP).

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-creating.png">

Once create successfully you should see similar screen

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-created.png">

- **Step 3.** Attach Virtual Private Gateway to your VPC. Select your newely created Gateway and click on *Actions* menu. Select *attach to VPC* option.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-attaching.png">

In the new window select your VPC based on your username to which Virtual Private Gateway will be attached.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-attaching-to-vpc.png">

Once done you should see status *attached* for your Virtual Private Gateway.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-attached.png">

- **Step 4.** Add tag to your Virtual Private Gateway. 

**THIS STEP IS REQUIRED AND MUST BE DONE BEFORE NEXT STEPS**

Select your Virtual Private Gateway, and click on Tags tab in the bottom working space. Press button *Add/Edit Tags*

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-enter-tag.png">

In the new window click *Create Tag*, and then add following tag (it must be exactly this one, no capital letters !)

  **Key:** transitvpc:spoke
  **Value:** true

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vgw-add-tag.png">

Once completed, select *Site-to-Site VPN connections* in the left menu.
Watch for new VPN connections  created between your new Virtual Private Gateway and CSR1000v virtual routers in Transit VPC.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpn-pending.png">

Wait until status will change to *available*

## Add routes for return traffic to on-premise Data Center

- **Step 1.** Select your Route Tables from the left menu, and find your VPC.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-rt-find.png">

- **Step 2.** Find route tables associated with your VPC. For this type your username in the search bar.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-rt-search.png">

- **Step 3.** Edit VPC Main Routing Table. Check in which row the *Main* column contains *Yes*. Select that route table (usually it does not have a name) and select Routes tab from the bottom panel. Click on *Edit routes* button here.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-rt-edit-route.png">

- **Step 4.** Add route to On-Premise data center. Enter following parameters:

  - **Prefix:** 172.18.0.0/24
  - **Target:** type *vgw-* and you will find your Virtual Private Gateway created earlier.

  Click *Save routes*

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-subnet-add-route.png">

- **Step 5.** Add the same return route under *subnets*. From the panel above select *studentXX-private-route-table1** only and add the same subnet as in Step 4.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-rt-subnet-edit.png">

- **Step 6.** Add route to On-Premise data center. Enter following parameters:

  - **Prefix:** 172.18.0.0/24
  - **Target:** type *vgw-* and you will find your Virtual Private Gateway created earlier.

  Click *Save routes*

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-vpc-subnet-add-route.png">

## Update Security Groups rules to allow traffic to on-premise Data Center

- **Step 1.** Select EC2 service

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-ec2-enter.png">

- **Step 2.** Find your EC2 instance (worker node), using your username in the search bar.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-ec2-find.png">

- **Step 3.** Update EC2 security group.

Select your EC2 instance. on the left side in the same row where your instance is, select Security Group. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-ec2-find-sg.png">

you will be redirected to Security Groups dashboard where you should select *Inbound* and then click on *Edit rules* button.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-sg-enter.png">

- **Step 4.** Add new rule to allow ingress traffic to EC2 instance from On-Premise prefix.

Add new rule with following parameters:

  - **Type:** All traffic
  - **Source:** 172.18.0.0/24

Click Save.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-sg-add-rule-prefix.png">

## Validate connectivity

From Linux jumphost machine, ping IP address of your EC2 instance. 
To find out your EC2 instance IP address, go to EC2 dashboard, search for your instance using your username. In the bottom panel in *Description* tab click on *Network Interfaces eth0* link. In the popup menu you will see IP address of the interface. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-ec2-eth0-ip.png">

You can try to ping this IP address from Linux Jumphost. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-vpn-validation.png">
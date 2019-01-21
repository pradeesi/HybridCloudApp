# Lab Task 2: Exploring Cisco Container Platform



Cisco Container Platform is a production grade platform to manage, monitor and deploy Kubernetes Clusters in your Enterprise. 
CCP uses 100% upstream Kuberenetes without vendor specific modification, creating seamless experience for developer to deploy application on any kubernetes platform in the public or private cloud.  

CCP provides authentication and authorization, security, high availability, networking, load balancing, and operational capabilities to effectively operate and manage Kubernetes clusters. CCP also provides a validated configuration of Kubernetes and can integrate with underlying infrastructure components such as Cisco HyperFlex and Cisco ACI. The infrastructure provider for CCP is Hyperflex.

Cisco Container Platform has two main architecture components:
- Control Plane Cluster - to provide management platform for your Kubernetes Clusters where you can deploy new, scale worker nodes, manage policy and networking. The Control Plane is also build based on Kubernetes.
- Tenant Data Cluster - the Kubernetes cluster used to host applications across production, development, staging and many other environments

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp_features.png">

Each user in this lab will have his own Cisco Container Platform Control Plane.  
As described in the Lab task 1, check Table 1 with the URL to access your CCP Control Plane cluster dashboard.

## 1. Explore CCP dashboard

Login to CCP Dashboard - find URL in [Table 1](../lab_task_1_environment_access.md), use your Active Directory credentials that you can find in `LTRCLD-2948_CCP_LAB` file in Google Sheet. 

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

## 2. Create Tenant Data Cluster

After login to Cisco Container Platform, click `New Cluster` button, you will be redirected to the new page where you would have to provide details of your new Kubernetes cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty.png">

- Step 1 - Basic Information - select infrastructure provider, Kubernetes cluster name and Container Network Interface:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step1.png">

_In this step you have selected "Calico" as a Container Networking Interface, however there are other two supported - Cisco ACI® and Contiv-VPP. Cisco ACI integration is done automatically during new Kubernetes cluster creation, CCP configures tenant in ACI with required network policies and Policy Based Routing that is used as a Load-Balancing services in hardware._

- Step 2 - Provider Settings - infrastructure provider details such as storage, vSwitch port-group and base image with approriate Kubernetes version:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step2.png">

_This lab is based on regular UCS servers, however, combination of Hyperflex and CCP result in best in class performance. CCP can automatically provision dynamic persistent volumes directly on Hyperflex, rather on vmware, bypassing extra layer of virtualisation._

- Step 3 - Node configuration - here you can configure node sizing, pass access information such as public SSH key, Load-Balancer VIP, subnet for PODs, enable service-mesh based on Istio 1.0 project and finally provide rigths for managing kubernetes clusters in AWS public cloud.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step3.png">

_Cisco Container Platform currently supports nodes created in VMware vSphere environment as Virtual Machines, however  Baremetal servers as a worker nodes will be supported in the next releases._

On the next screen you will see option to enable `Harbor Registry`, please **do not** select this option at this point.  

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step4.png">

Click Next to enter the summary page, and there just confirm that all data are valid according to google sheet. Once confirmed please click `Finish`.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step5.png">

Once finished, you will see progress bar to check status of the cluster creation.

## 3. Monitor cluster creation

You can observe tenant cluster creation from CCP Dashboard, however, if you are interested to see more details, you can login to vCenter and monitor VM cloning process.
Users are grouped by PODs, each POD is managed by single VMWare vCenter instance. Please use respective vCenter for your POD:  

Open chrome browser, and enter URL of vCenter `https://vc-pod0X`. **Perform all operations from jumphost:**

To avoid issues with Flash Player, please select HTML5 mode for vCenter User Interface:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/vcenter-select-html-flash.png">

Login to vCenter using Single Sign-On plugin, just click on `Use Windows session authentication` and allow plugin to run. You can also disable this prompt for future by unchecking option `Ask always before allowing this site`.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/vcenter-login-page-SSO.png">

Once logged-in, you can observe cloning process:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/vcenter-html-cloning.png">

_Please note that multiple users may perform similar operation at the same time, therefore you may see multiple cloning processes._

## 4. Kubernetes Data Cluster administration

Once cluster installation has finished, you will see the status 
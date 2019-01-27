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

Login to your dedicated CCP Dashboard - find URL in [Table 1](../lab_task_1_environment_access.md), use your Active Directory credentials that you can find in paper sheet on your desk.

Once logged in, you will be taken to the "cluster" page.
In this page you can manage your kubernetes clusters, edit their configuration, adding nodes or create node policies.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty.png">

In the left pane you will see other options such as `User management`, where users or group of users are managed locally or authentication could be integrated with Active Directory services. In our lab, Cisco Container Platform has been integrated with Active Directory.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-user-mgmt-ad.png">

In the next menu position, you will see `Infrastructure Providers`. This is place where you select your cloud infrastructure, either it could be on-prem VMware vSphere or public cloud - Amazon Web Services.  Cisco Container Platform requests resources such as virtual machines that later on will act as master and worker nodes of your Kubernetes cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-infra-providers-vmware.png">

`Networks` provides IP addressing subnets and pools configuration for the tenant clusters. When tenant cluster is deployed, the IP addresses for nodes are allocated from DHCP, however, Cisco Container Platform provides built-in mechanism to allocate IP addresses for Service Expousure under which applications will be exposed externally. This mechanism is explaining later in the lab 3 **add reference to lab with VIP pools**

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-networks-main.png">

The last tab contains `Licensing`, where you can register your Cisco Container Platform with Smart Licensing server.

## 2. Create Tenant Data Cluster

After login to Cisco Container Platform, click `New Cluster` button, you will be redirected to the new page where you would have to provide details of your new Kubernetes cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty.png">

- Step 1 - Basic Information - select infrastructure provider, Kubernetes cluster name and Container Network Interface:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step1.png">

_In this step you have selected "Calico" as a Container Networking Interface, however there are other two supported - Cisco ACI and Contiv-VPP. Cisco ACI integration is done automatically during new Kubernetes cluster creation, CCP configures tenant in ACI with required network policies and Policy Based Routing that is used as a Load-Balancing services in hardware._

- Step 2 - Provider Settings - infrastructure provider details such as storage, vSwitch port-group and base image with approriate Kubernetes version:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step2.png">

_This lab is based on regular UCS servers, however, CCP in combination with Cisco hyperconverged infrastructure - Hyperflex results in best in class performance. CCP can automatically provision dynamic persistent volumes directly on Hyperflex, rather on vmware, bypassing extra layer of virtualisation._

- Step 3 - Node configuration - here you can configure node sizing, pass access information such as public SSH key, Load-Balancer VIP, subnet for PODs, enable service-mesh based on Istio 1.0 and finally provide rigths for managing kubernetes clusters in AWS public cloud.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step3.png">

_Cisco Container Platform currently supports nodes created in VMware vSphere environment as Virtual Machines, however Baremetal servers as a worker nodes will be supported in the next releases._

On the next screen you will see option to enable `Harbor Registry`, to enable local docker image. At this point please **do not** select this option.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step4.png">

Click Next to enter the summary page, and just confirm all data are valid according to google sheet. Once confirmed please click `Finish`.

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

## 4. Kubernetes Data Cluster access and administration

Once cluster installation has finished, you will see the status `READY` in CCP dashboard.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-cluster-ready.png">

Accessing new Kubernetes cluster requires to obtain the kubeconfig file. Click on the arrow on the right side of the cluster name to see additional options. Select `Download kuberconfig`. File will be downloaded on your desktop.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-cluster-access-dashboard.png">

From the same context menu you can enter to detailed more of the cluster, access Kubernetes dashboard or monitoring based on Prometheus and Kibana or even a delete cluster.

Next task is to enter into the detailed view of the cluster, here you can also download kubeconfig file.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-cluster-edit-details-2.png">

Next, click on the `Kubernetes Dashboard` button:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-cluster-access-dashboards.png">

You will be redirected to Kubernetes standard dashboard. Cisco did not changed the Kubernetes User Interface intentionaly, since it is well known by developers. 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-cluster-access-dashboard.png">

Please select `Kubeconfig` option (which is the default) and select previously stored kubeconfig.yaml file which should be in the `Downloads` folder.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-select-kubeconfig.png">

Once selected, click Sing-In:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-kubeconfig-selected.png">

After successful login you will be redirected to the default namespace view:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-default-view.png">

## 5. Kubectl - Kubernetes command line interface

While most of the options in Kubernetes are available through the dashboard, CLI commands are also available, and convenient to use. Kubectl is a software leveraging Kubernetes API and translate commands to specific API calls.  
You can install `kubectl` directly on your PC or jumphost, or login to master node of your Kubernetes Cluster. 

To install `kubectl` application, go to <link> and follow instruction.

Kubectl requires credentials to operate on your Kubernete Cluster. By default `.kube` folder is created in your User folder in Windows (similarily on Linux and MAC). Please copy downloaded `kubeconfig.yaml` file as described in previous section to this folder.

You can now open command line in Windows (start -> type `kubectl`) and terminal window will appear. 
Please execute following command to verify `kubectl` can operate on your cluster.

    kubectl get nodes -o wide

Alternatively, you can login via SSH to your Master node using PuTTY application available on your desktop on the jumphost. 
Login to Kubernetes node require SSH private key. The Key is located on the Jumphost in the folder `C:\ssh-key\id_rsa.pem`

Open PuTTY, go to SSH option and select private key, next go to Data and provide username `ccpuser`.
Once logged in to Kubernetes master node, you can use `kubectl` command without kubeconfig (since it is already included in the environment variables.

## 6. Accessing Grafana dashboard

Once you are logged in to Kubernetes cluster dashboard, you can obtain password to grafana dashboard which provides grafical view of Kubernetes cluster condition, but also to monitor your applications. 

Passwords are stored in Kubernetes Secrets object. Grafana admin password can be decoded from base64 encryption, and copy-pasted to grafana login page.

Next steps will show you how to find grafana password:

First, change namespace to `CCP`:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-cluster-access-dashboard.png">

Next, go to `Secrets` object in the menu, and look and the main pane on the right, you will be looking for secret called `ccp-monitor-grafana`


<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-ccp-secrets-1_2.png">

Got to second page and there you will find desired Secret.  

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-ccp-secrets-2_2.png">

In the `Data` field you will see admin-password and small eye icon. Please click on that icon to uncover the password. Once uncovered please copy it to clipboard.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/k8s-ccp-grafana-password.png">  

Alternatively, you can use following one-line `kubectl` command to obtain grafana admin-password. Please use this command from the master node, rather local PC as it may not have base64 installed.

    kubectl get secret -n ccp grafana-monitor | base64 --decode

Next, please go back to the CCP dashboard, select your cluster, go into the detail mode and select `Grafana` button.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-grafana-button.png">


You will be redirected to the Grafana page, where you can login with username `admin` and copied password from Secret.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/grafana-login.png">

Once logged to grafana, please select in the top left corner `Home` drop down menu, and select `Prometheus`. The dashboard where you can monitor resource utilisation of all PODs across all namespaces.


< paste screenshot >


## 7. Accessing logs on Cisco Container Platform

In a container environment ...

Cisco Container Platform has build in logging stack leveraging projects such Elasticsearch, Fluentd and Kibana (in short it is called EFK stack). 
Fluentd normalizes logs from different endpoints to a consumable format used later on by Elasticsearch.
Elasticsearch - ....
Kibana - grafical user interface to quickly browse, find and create custom reports.

By default access to Kibana is not exposed due to security reasons. The quickest way to login to Kibana is to setup port-forwarding towards POD where kibana has been deployed. Use your installed `kubectl` CLI client on windows and enter following command:

    kubectl port-foward -n ccp kibana-monitor-XXX 5061:5061
    
Open Chrome web-browser, and enter following URL:

    https://localhost:5061

Once page will be opened, go to the `Search` option and type in the filter list 

    logstash-*

After this, you will be able to see logs from all PODs and applications working on this cluster. 

Furthe filtering could be appliend, but this is not the main topic of this lab excercise. 




## Create Tenant Data Cluster

After login to Cisco Container Platform, click `New Cluster` button, you will be redirected to the new page where you would have to provide details of your new Kubernetes cluster.

During creation, you will be asked to specify some parameters. Please open google sheet and find your POD ID in the tab.

[_**Google Sheet**_](https://docs.google.com/spreadsheets/d/1r81v_Mb-GKGV-d3GNoMygn4JIsF2UeRC3JTDz-sN48s/edit?usp=sharing)

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-clusters-empty.png">

- Step 1 - Basic Information - select infrastructure provider, Kubernetes cluster name and Container Network Interface:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step1.png">

_In this step you have selected "Calico" as a Container Networking Interface, however there are other two supported - Cisco ACI and Contiv-VPP. Cisco ACI integration is done automatically during new Kubernetes cluster creation, CCP configures tenant in ACI with required network policies and Policy Based Routing that is used as a Load-Balancing services in hardware._

- Step 2 - Provider Settings - infrastructure provider details such as storage, vSwitch port-group and base image with approriate Kubernetes version:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step2.png">

_This lab is based on regular UCS servers, however, CCP in combination with Cisco hyperconverged infrastructure - Hyperflex results in best in class performance. CCP can automatically provision dynamic persistent volumes directly on Hyperflex, rather on vmware, bypassing extra layer of virtualisation._

- Step 3 - Node configuration - here you can configure node sizing, provide access information such as public SSH key, Load-Balancer VIP, subnet for PODs.  

**Do not** enable service-mesh based on Istio 1.0 and finally provide rigths for managing kubernetes clusters in AWS public cloud.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step3-1.png">

On the next screen you will see option to enable `Harbor Registry`, to enable local docker image. At this point please **do not** select this option.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step4.png">

Click Next to enter the summary page, and just confirm all data are valid according to google sheet. Once confirmed please click `Finish`.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-create-cluster-step5.png">

Once finished, you will see progress bar to check status of the cluster creation.

## Monitor cluster creation

You can observe tenant cluster creation from CCP Dashboard, however, if you are interested to see more details, you can login to vCenter and monitor VM cloning process.

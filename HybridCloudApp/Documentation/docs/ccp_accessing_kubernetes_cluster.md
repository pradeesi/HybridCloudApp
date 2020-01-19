## Accessing Kubernetes Cluster

## Kubectl - Kubernetes Command Line Interface

While most of the options in Kubernetes are available through the dashboard, CLI commands are also available, and convenient to use. Kubectl is a software leveraging Kubernetes API and translate commands to specific API calls. This tool will be used during the lab.

Once connectivity to your new EKS Kubernetes Cluster is confirmed, go back to Cisco Container Platform (CCP) web page, login if required and select Clusters -> AWS to display your newely created Kubernetes EKS cluster.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-ready.png">

- **Step 1:** Accessing new Kubernetes cluster requires to obtain the kubeconfig file. Click on the name of your cluster to see the detailed view.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-download-kubeconfig.png">

- **Step 2:** Copy kubeconfig file to your linux jumphost machine using SCP. Open WinSCP from the desktop, and login to Linux Jumphost using your credentials.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/scp.png">

Copy kubeconfig file into your home directory (this is the directory opened after successful login)

- **Step 3:** Merge EKS kubeconfig file with existing kubeconfig file for on-premise Kubernetes.
SSH to Linux machine using PuTTY, change directory to *.kube* and list files, you should notice file *on-prem.yaml*.

        ls -la
        cd .kube
        ls -la

Merge kubeconfig files so you will be able to switch between contexts using kubectl tool, rather specifying full path to your kubeconfig file in every command.
This command will merge kubeconfig files and create new file in `~/.kube/config`. This is the default location for kubectl to find access information to particular Kubernetes Cluster.

        KUBECONFIG=~/.kube/on-prem.yaml:~/kubeconfig.yaml kubectl config view --flatten > ~/.kube/config

List files again in `~/.kube/config` directory to make sure that new `config` file is there.

- **Step 4:** Kubeconfig file usually contains private certificate that is uathorized by kubernetes directly. In case of EKS, AWS IAM authenthentication is involved. Instead of certiciate, we will use your AWS access keypair to authenticate. On the linux jumphost, aws cli tool is installed. Similarily to kubectl this tool provides management access to your AWS account. Using this tool you can spawn new VM or create new networking infrastructure like VPC, subnets etc. In this lab, aws cli is leveraged by IAM-Authenticator module to sign-up kubectl requests towards EKS. 

Obtain login access keypair from AWS webpage first:

Login to AWS Dashboard, click on your username in the top right corner and select *My Security Credentials*.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-access-key-enter.png">

- **Step 5:** Create new Access Key

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-access-key-create-new.png">

in the new window obtain access key ID and secret by copying it to clipboard.

In the Linux jumphost, type:

        aws configure

and paste access key ID and secret that you obtained from AWS webpage.


From now you can switch contexts to access and send commands to Kubernetes cluster in AWS or on-premise Data Cetner.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-import-eks-kubeconfig.png">
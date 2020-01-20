# Accessing Kubernetes Cluster

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
SSH to Linux machine using PuTTY, confirm that your kubeconfig.yaml file has been copied to home directory

        ls -l

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-kubeconfig-in-home.png">

change directory to *.kube* and list files, you should notice file *on-prem.yaml*.

        cd .kube
        ls -l

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-on-prem-in-kube.png">

Merging kubeconfig files let you switch between contexts using kubectl tool, rather specifying full path to your kubeconfig file in every command.
This command will merge kubeconfig files and create new file in `~/.kube/config`. This is the default location for kubectl to find access information to particular Kubernetes Cluster.

        KUBECONFIG=~/.kube/on-prem.yaml:~/kubeconfig.yaml kubectl config view --flatten > ~/.kube/config

List files again in `~/.kube/config` directory to make sure that new `config` file is there.

        ls -la

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-kubeconfig-merge.png">

- **Step 4:** Kubeconfig file usually contains private certificate that is uathorized by kubernetes directly. In case of EKS, AWS IAM authenthentication is involved. Instead of certiciate, we will use your AWS access keypair to authenticate. On the linux jumphost, aws cli tool is installed. Similarily to kubectl this tool provides management access to your AWS account. Using this tool you can spawn new VM or create new networking infrastructure like VPC, subnets etc. In this lab, aws cli is leveraged by IAM-Authenticator module to sign kubectl requests towards EKS using Secure Token Service (STS) in AWS.

- **Step 5 :** Obtain login access keypair from AWS webpage first

Login back to AWS Dashboard, click on your username in the top right corner and select *My Security Credentials*.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-access-key-enter.png">

- **Step 6:** Create new Access Key

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-access-key-create-new.png">

in the new window obtain access key ID and secret by copying it to clipboard.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-access-cred.png">

**IMPORTANT NOTE** Secret key is only shown during creating key. If you close window with sectet, you cannot view it anymore. Make sure to not close this window during copy-pasting credential information to terminal in Step 6.

- **Step 7:** Configure aws cli with your access key.

In Linux jumphost console, type:

        aws configure

paste access key ID and secret that you obtained from AWS webpage.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-cli-configure.png">

Validate if your kubeconfigs has been correctly imported:

        kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-get-contexts-wo-ns.png">

The star in front of cluster means which Kubernete Cluster context is used. 

- **Step 8:** For EKS Cluster, you will have full admin rights, however on-premise Kubernetes Cluster is shared with with other students, therefore you will have access only to your namespace. To avoid typing namespace in every `kubectl` command, configure default namespaces in your contexts using followng commands

        kubectl config set-context aws --namespace default
        kubectl config set-context on-prem-1 --namespace studentXX    ## XX - use your username ID.

List updated contexts:

        kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/linux-kubectl-set-namespaces.png">

If you would like to change context to aws EKS Kubernetes Cluster, please use following command:

        kubectl config use-context aws
        kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-use-aws.png">

Validate your access and list Kubernetes nodes in AWS EKS Cluster

        kubectl get nodes

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-get-nodes-aws.png">

To change context to on-premise Kuberenetes Cluster use follwing command:
        
        kubectl config use-context on-prem-1
        kubectl config get-contexts

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-use-on-prem.png">

Validate your access and list Kubernetes nodes in on-premise Cluster

        kubectl get nodes

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/kubectl-get-nodes-on-prem.png">
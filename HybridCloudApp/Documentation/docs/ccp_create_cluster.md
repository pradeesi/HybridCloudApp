## Create Tenant Data Cluster

After login to Cisco Container Platform, got to AWS tab and click `New Cluster` button. You will be redirected to the new page where you will provide details of your new Kubernetes EKS cluster.

- **Step 1:** Basic Information - select infrastructure provider, AWS Region and Kubernetes cluster version and name. Please use following parameters.

  - **Infrastructure Provider:** *aws*
  - **AWS Region:** *eu-central-1*
  - **Kubernetes Version:** *1.14*
  - **Kubernetes Cluster Name:** *studentXX*

studentXX - XX is your unique student ID.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-basic-info.png">

- **Step 2:** Node Contfiguration - here you will configure how EKS nodes will be setup. You will specify EC2 instance type, AMI image, number of worker nodes, IAM Role and SSH public key, so you could ssh into the node for troubleshooting purposes. 
**Please use exact paramaters as instruction says.**

  - **Instance Type:** *t2.small*

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-instance-type.png">

  - **Machine Image:** select image 

you may need to click on *Show filtered options* first

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-ami-filtered.png">

Select image (you should see only one)

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-ami.png">

  - **Worker Count:** *Please decrease to* **1**

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-worked-count.png">

  - **IAM Access role ARN:** *type here your username, and select role accociated to your user, i.e.* **student17-role**

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-iam-role.png">

Your AWS user is configured with IAM policy that allows to assume this specific role. For this CCP leverages IAM-Authenticator add-on, that is installed in Linux jumphost. Later on the Linux machine You will login to your aws cli with your associated aws credentials and then you will be able to manage you new EKS Kubernetes Cluster. Instead of using username and password or private certificates, IAM Authenticator leverages AWS STS (Secure Token Service) to tokenize and sign URL requests towards your EKS Cluster. AWS IAM is responsible to authorize request and pass commands to your Kubernetes Cluster.
During creation of EKS Cluster, this role is associated with Kubernets System:Masters group which provides full access to your cluster.

  - **SSH Public Key:** Paste following ssh key into the CCP

    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJeLi4z9dYE+6tqTXzsELMch2RjR6R+rl57UEJzMuPkO

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-sshkey.png">

-- **Step 3:** VPC configuration - here specify your VPC subnets. CCP will request VPC creation in AWS, with subnets, internet gateway, nat gateways. It is creating 3 private and 3 public subnets. Please modify default subnet's second octet only to match your username ID (ie. for studnet17 it will be 10.17.0.0/16 in the Subnet CIDR, and following Public and Private subnets must fall behind main VPC subnet, 10.17.0.0/24, 10.17.1.0/24 etc.)

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-vpc.png">

CCP will create for each cluster following network topology in AWS:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-eks-vpc-topology.png">

Click Next to enter the summary page, and just confirm all data. Once confirmed please click `Finish`.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-summary.png">

Once finished, you will see progress bar to check status of the cluster creation.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-creating.png">

## Monitor cluster creation

You can observe tenant cluster creation from CCP Dashboard, however, if you are interested to see more details, you can login to AWS dashboard and go to EKS to monitor master creation, and then to CloudFormation to see status of CloudFormation Stack deployment. CloudFormation is a AWS tool to automate creation of different objects.

Login to AWS dashboard, and select EKS service.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-eks-find.png">

In EKS dashboard you will see EKS service creation progress. Once finished you can move to CloudFormation dashboard.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-cloudformation-find.png">

From there find your stack (based on your username) and watch deployment progress.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/aws-cloudformation-watch.png">

Once finished, you should see in CCP GUI that the Kubernetes Cluster in AWS has been deployed successfully.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp5-eks-ready.png">

At this point go to the next chapter to connect your Kubernetes Cluster in AWS to Hybrid Network that provides access to on-premise Data Center.
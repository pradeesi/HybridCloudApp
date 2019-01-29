## Accessing Kubernetes Cluster

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

## Kubectl - Kubernetes Command Line Interface

While most of the options in Kubernetes are available through the dashboard, CLI commands are also available, and convenient to use. Kubectl is a software leveraging Kubernetes API and translate commands to specific API calls.  
You can download `kubectl` directly on your PC or jumphost, or login to master node of your Kubernetes Cluster. 

`kubectl` can be donwloaded fro this [LINK](https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/windows/amd64/kubectl.exe) and follow instruction.

Kubectl requires credentials to operate on your Kubernete Cluster. By default `.kube` folder is created in your User folder in Windows (similarily on Linux and MAC). Please move  downloaded `kubeconfig.yaml` file as described in previous section to this folder and change name to `config` without file extension.

You can now open command line in Windows (start -> type `kubectl`) and terminal window will appear. 
Please execute following command to verify `kubectl` can operate on your cluster.

    kubectl get nodes -o wide

Alternatively, you can login via SSH to your Master node using PuTTY application available on your desktop on the jumphost. 
Login to Kubernetes node require SSH private key. The Key is located on the Jumphost in the folder `C:\ssh-key\id_rsa.pem`

Open PuTTY, go to SSH option and select private key, next go to Data and provide username `ccpuser`.
Once logged in to Kubernetes master node, you can use `kubectl` command without kubeconfig (since it is already included in the environment variables.

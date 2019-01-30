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

You can login via SSH to your Master node using PuTTY application available on your desktop on the jumphost. 

* **Step 1** Obtain IP address of your Kubernetes Master node.

Login to Cisco Container Platform, go to the details of you cluster and see the IP address of your Kubernetes Master node. Note there are two addresses, one is VIP and one is a real Node IP address assigned by DHCP. You can use either one.  

* **Step 2** SSH to Master Node using PuTTY

Login to Kubernetes node require SSH private key. The Key is located on the Jumphost in the folder `C:\ssh-key\id_rsa.pem`. 

Open PuTTY, go to `Connection -> SSH -> Auth` and select private key - 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/putty-private-key.png" width=500>

next go to `Connection -> Data` and provide username `ccpuser` -  

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/images/putty-username.png" width=500>

Once logged in to Kubernetes master node, you can use `kubectl` command. You can try example command to obtain nodes information.

    kubectl get nodes -o wide
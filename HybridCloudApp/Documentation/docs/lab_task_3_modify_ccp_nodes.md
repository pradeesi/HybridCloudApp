# LAB Task 3 Cisco Container Platform - modify node configuration

By default, when new cluster is created, it puts Master node and Worker nodes to separate pools of nodes. 
The reason behind it is to not deploy applications on the master node.

This lab should be executed once your application has been deployed, on your Kubernetes cluster. One of the application components - REST APi agent is running on two worker nodes, since the replica has been set to 2.
Let's try to remove one node from the cluster, and check how Kubernetes will maintain two copies of the POD.

Login to Cisco Container Platform dashboard, and select your Kubernetes cluster (click on its name)

<img >

Select `default-pool` and click on the small square to edit it's settings.  
Decrease number of nodes to one and save

<img >

Use kubectl command to check pods discritbution across worker nodes:

    Kubectl get pods -o wide
    
    < paste output >
    
you should see that the number of pods for REST API service is still two, however they are all deployed on single node. 

Let's add back second node, this time using new pool:

Edit your Kubernetes cluster, click `New Node Pool` button

Enter name of the new pool - for example POOL-DB-ONLY

In the creator, you will see additional fields to provide Labels and Taints,

Taint is a special label that prevents particular POD with label to be deployed on this node. 

For example, we would like to dedicate this new node only for database type PODs, due to hardware configuration is using SSD disks for high performance cache.
Add Taint label as following:

    Type : web, app
    Select Action: NoSchedule
    
<img >

From now, any POD with the label `web` or `app` could not be deployed


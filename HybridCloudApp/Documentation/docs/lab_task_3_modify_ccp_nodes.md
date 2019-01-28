# LAB Task 3 Cisco Container Platform - modify node configuration

By default, when new cluster is created, it puts Master node and Worker nodes to separate pools of nodes. 
The reason behind it is to not deploy applications on the master node.

This lab should be executed once your application has been deployed, on your Kubernetes cluster. One of the application components - REST APi agent is running on two worker nodes, since the replica has been set to 2.
Let's try to remove one node from the cluster, and check how Kubernetes will maintain two copies of the POD.

Execute first command to verify original POD distribution across nodes:

    kubectl get pods -o wide

    ccpuser@pod06-a-ccp-data-master40bae43bca:~$ kubectl get pods -o wide
    NAME                                          READY     STATUS    RESTARTS   AGE       IP            NODE                                NOMINATED NODE
    iot-backend-mariadb-6bbf6f4764-qxw6g          1/1       Running   0          1h        10.161.2.15   pod06-a-ccp-data-workerf49047e761   <none>
    iot-backend-mqtt-db-agent-57c88c58dd-wcbvs    1/1       Running   0          22m       10.161.2.21   pod06-a-ccp-data-workerf55c089976   <none>
    iot-backend-rest-api-agent-75bfb74dc4-bd52b   1/1       Running   0          22m       10.161.2.19   pod06-a-ccp-data-workerf49047e761   <none>
    iot-backend-rest-api-agent-75bfb74dc4-dgvbk   1/1       Running   0          34s       10.161.3.4    pod06-a-ccp-data-workerf55c089976   <none>

Next, login to Cisco Container Platform dashboard, and select your Kubernetes cluster (click on its name)

Click on the small square next to `default-pool` to edit it's settings.  

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-modify-worker-pool-edit.png">

Decrease number of nodes to one and save

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-modify-cluster- decrease-number.png" width=500>

Use kubectl command to check pods discritbution across worker nodes:

    kubectl get pods -o wide
    
    ccpuser@pod06-a-ccp-data-master40bae43bca:~$ kubectl get pods -o wide
    NAME                                          READY     STATUS    RESTARTS   AGE       IP            NODE                                NOMINATED NODE
    iot-backend-mariadb-6bbf6f4764-qxw6g          1/1       Running   0          1h        10.161.2.15   pod06-a-ccp-data-workerf49047e761   <none>
    iot-backend-mqtt-db-agent-57c88c58dd-wcbvs    1/1       Running   0          22m       10.161.2.21   pod06-a-ccp-data-workerf49047e761   <none>
    iot-backend-rest-api-agent-75bfb74dc4-bd52b   1/1       Running   0          22m       10.161.2.19   pod06-a-ccp-data-workerf49047e761   <none>
    iot-backend-rest-api-agent-75bfb74dc4-dgvbk   1/1       Running   0          34s       10.161.3.4    pod06-a-ccp-data-workerf49047e761   <none>
    
you should see that the number of pods for `iot-backend-rest-api-agent` PODs  is still two, however they are all deployed on single node. 

_it may take several minutes until node will be removed, since Kubernetes must move PODs running on the removed node to the node that will stay within cluster. Sometimes the other node must download image, since that kind of POD was never deployed before_

Once node will be removed, please execute `kubectl get pods -o wide` and note how PODs are distributed.

Let's add back second node - again edit to default-pool and increase number of nodes to `2`

Execute `kubectl get nodes -o wide` to check status of the node deployment. Once status will be `READY`, verify how PODs are distributed.

Note that adding node to the cluster does not change distribution of PODs automatically. In order to force Kubernetes to deploy POD on the second node, please delete one of the POD `iot-backend-rest-api-agent`

    kubectl delete pod iot-backend-rest-api-agent-XXXXXX 

once this is completed verify what happend with `kubectl get pods -o wide` command.

During delete operation, Kubernetes realized that POD should have 2 replicas, therefore, it deployed one more replica on the next worker node in the pool.

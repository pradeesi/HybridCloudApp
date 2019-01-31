## Accessing Grafana dashboard

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

** This command works only in linux environment, you can use it on the Kubernetes master node to which you can SSH **

    kubectl -n ccp get secret ccp-monitor-grafana -o=jsonpath='{.data.admin-password}' | base64 --decode

Next, please go back to the CCP dashboard, select your cluster, go into the detail mode and select `Grafana` button.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-grafana-button.png">


You will be redirected to the Grafana page, where you can login with username `admin` and copied password from Secret.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/grafana-login.png">

Once logged in to grafana, please select in the top left corner `Home` drop down menu - 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-grafana-home.png"> 

select `Kubernetes Cluster Monitoring (Prometheus)`. The dashboard where you can monitor resource utilisation of all PODs across all namespaces.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-grafana-select-source.png">

You should see graphs like this - 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-grafana-dashboard.png">

## 7. Accessing logs on Cisco Container Platform

The Elasticsearch, Fluentd, and Kibana (EFK) stack enables you to collect and monitor log data from containerized applications for troubleshooting or compliance purposes. These components are automatically installed when you install Cisco Container Platform.

Fluentd is an open source data collector. It works at the backend to collect and forward the log data to Elasticsearch.

Kibana is an open source analytics and visualization platform designed to work with Elasticsearch. It allows you to create rich visualizations and dashboards with the aggregated data.

By default access to Kibana is not exposed due to security reasons. You can expose Kibana to the external network by using 'NodePort'. Let's check wherher kibana service exists currently:

    kubectl -n ccp get svc -n ccp
    NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)                      AGE
    ccp-efk-kibana                              ClusterIP      10.103.179.126   <none>         5601/TCP                     1d
    ccp-monitor-grafana                         ClusterIP      10.99.197.50     <none>         80/TCP                       1d
    ccp-monitor-prometheus-alertmanager         ClusterIP      10.105.91.170    <none>         80/TCP                       1d
    ccp-monitor-prometheus-kube-state-metrics   ClusterIP      None             <none>         80/TCP                       1d
    ccp-monitor-prometheus-node-exporter        ClusterIP      None             <none>         9100/TCP                     1d
    ccp-monitor-prometheus-pushgateway          ClusterIP      10.103.53.72     <none>         9091/TCP                     1d
    ccp-monitor-prometheus-server               ClusterIP      10.99.248.1      <none>         80/TCP                       1d
    elasticsearch-logging                       ClusterIP      10.101.23.250    <none>         9200/TCP                     1d
    kubernetes-dashboard                        ClusterIP      10.106.224.153   <none>         443/TCP                      1d
    nginx-ingress-controller                    LoadBalancer   10.99.88.25      172.18.1.239   80:32290/TCP,443:31442/TCP   1d
    nginx-ingress-default-backend               ClusterIP      10.103.155.52    <none>         80/TCP                       1d

**Note** the service `TYPE` of the `ccp-efk-kibana`. Currently it is ClusterIP, which is not reacheable outside of the Cluster.
In order to expose Logging dashboard (Kibana) for administrator, you can change `ClusterIP` service type to `NodePort` using following command:

    kubectl -n ccp edit svc ccp-efk-kibana

You will be taken to the `vi` editor. Please move arrows until line 3rd line from the bottom:

    (...)
      type: ClusterIP
    status:
      loadBalancer: {}

Change mode to edit using combination of keys in following order: `ESC` then press `i`. 

Change value `ClusterIP` to `NodePort`, please pay attention to capital letters. Like this:


    (...)
      type: NodePort
    status:
      loadBalancer: {}

Press `Esc` to exit from editing mode.

Press following combination of keys to save file in the following sequnce `:` then type `wq` then press `enter`

Confirm that the change has been successfully saved and execute following command to confirm service `type` for `ccp-efk-kibana`

    kubectl -n ccp get svc
    NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)                      AGE
    ccp-efk-kibana                              NodePort       10.97.166.41     <none>         5601:30662/TCP               11h

**Note** external service port, in above example it is `30662`. 

Check node IP addresses by using following command:

    kubectl get nodes -o wide

**Note** any IP address of your node in the collumn `External-IP`

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-get-nodes-ip.png">

Open Chrome web-browser, and enter following URL:

    http://<node_ip>:30662

In the instruction example: http://172.18.1.240:30662

Once page will be opened, you will be asked to create index pattern. It means, you have to point from which log collection the logs will be presented.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-kibana-home.png">

Click on Management and type `logstash-*` in the field - 

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-kibana-create-index.png">

Next, you will be asked to add additional pattern to the presented logs

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-kibana-create-index-2.png">

After this, you will be able to see logs from all PODs and applications working on this cluster. To do this, go to Discovery panel, and type in the filter at the top of the page:

    kubernetes.namespace.name = default

Since our application is deployed in default namespace, filter will show only logs from pods deployed in that namespace.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp-kibana-log-filter.png">

Further filtering could be appliend, but this is not the main topic of this lab excercise. 

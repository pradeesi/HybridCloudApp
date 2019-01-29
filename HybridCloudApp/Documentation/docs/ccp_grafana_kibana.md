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

By default access to Kibana is not exposed due to security reasons. The quickest way to login to Kibana is to setup port-forwarding towards POD where kibana has been deployed. Use your installed `kubectl` CLI client on windows and enter following command:


    # kubectl get pods -n ccp
    
    NAME                                                         READY   STATUS      RESTARTS   AGE
    ccp-efk-elasticsearch-curator-1548378000-7x2nd               0/1     Completed   0          2d
    ccp-efk-elasticsearch-curator-1548464400-9dzxv               0/1     Completed   0          1d
    ccp-efk-elasticsearch-curator-1548550800-gbv26               0/1     Completed   0          20h
    ccp-efk-kibana-6d7c97575c-gqjvg                              1/1     Running     0          2d
    ccp-monitor-grafana-84d4f8b644-nqpdl                         1/1     Running     0          2d
    ccp-monitor-grafana-set-datasource-llvlc                     0/1     Completed   3          2d
    ccp-monitor-prometheus-alertmanager-64c4f944cb-zxc2c         2/2     Running     0          2d
    ccp-monitor-prometheus-kube-state-metrics-5b6855c558-lcpff   1/1     Running     0          2d
    ccp-monitor-prometheus-node-exporter-48hh2                   1/1     Running     0          2d
    ccp-monitor-prometheus-node-exporter-9wbb9                   1/1     Running     0          2d
    ccp-monitor-prometheus-pushgateway-7cfbcd8dfd-s625f          1/1     Running     0          2d
    ccp-monitor-prometheus-server-6fb9957f87-r7s29               2/2     Running     0          2d
    elasticsearch-logging-0                                      1/1     Running     0          2d
    fluentd-es-v2.0.2-8d6rm                                      1/1     Running     0          2d
    fluentd-es-v2.0.2-hljg5                                      1/1     Running     0          2d
    kubernetes-dashboard-5888c7c865-psk88                        1/1     Running     0          2d
    metallb-controller-54559b4447-2rftf                          1/1     Running     0          2d
    metallb-speaker-8pzdw                                        1/1     Running     0          2d
    metallb-speaker-rtbp4                                        1/1     Running     0          2d
    nginx-ingress-controller-fxg78                               1/1     Running     0          2d
    nginx-ingress-controller-h8nk6                               1/1     Running     0          2d
    nginx-ingress-default-backend-57fb689dd7-gx6sl               1/1     Running     0          2d

    kubectl port-foward -n ccp ccp-efk-kibana-<id> 5601:5601

    example:
    kubectl port-foward -n ccp ccp-efk-kibana-6d7c97575c-gqjvg 5601:5601
    
Open Chrome web-browser, and enter following URL:

    https://localhost:5061

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

Furthe filtering could be appliend, but this is not the main topic of this lab excercise. 

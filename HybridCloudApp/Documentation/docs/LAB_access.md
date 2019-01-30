# Connectivity Check

## 1. Lab access general description

The lab has been built leveraging multiple cloud environments as following:

- Amazon Web Services
- Google Cloud
- Private intrastructure on-prem

During this lab, you will get access to Google Cloud and Private Infrastructure, as these are providing container environment. Amazon Web Services is used in this setup as a message broker only which is a function already provided by Amazon. 


## 2. On-prem private infrastructure access

In order to get access to private network, please first find credentials for your POD in the paper sheet on in the DMZ_USER_XX.txt file on the desktop. 

Each LAB User will have dedicate instance on Cisco Container Platform, where you can manage Kubernetes Cluster. Once you will create Kubernetes cluster, you will deploy your containerized application.

_Multiple are using same server, hence the naming POD0X-Y where X is a server number and Y is a environment ID within that server. Servers are running ESXi, and each ESXi is managed by own vCenter.
Two to five users will share the same hardware server and same vCenter, however each User will have own instance of Cisco Container Platform._

Below table provides URLs to User's on-prem environment

*Table 1: User to POD assignment*

VPN/AD User | POD name | vCenter URL | CCP Control Plane URL
--- | --- | --- | ---
DMZ_User_01 | POD 01-A | https://vc-pod01.hybridlab.local | https://172.18.1.165
DMZ_User_02 | POD 01-B | https://vc-pod01.hybridlab.local | https://172.18.1.169
DMZ_User_03 | POD 01-C | https://vc-pod01.hybridlab.local | https://172.18.1.173
DMZ_User_04 | POD 02-A | https://vc-pod02.hybridlab.local | https://172.18.1.177
DMZ_User_05 | POD 02-B | https://vc-pod02.hybridlab.local | https://172.18.1.181
DMZ_User_06 | POD 02-C | https://vc-pod02.hybridlab.local | https://172.18.1.185
DMZ_User_07 | POD 03-A | https://vc-pod03.hybridlab.local | https://172.18.1.189
DMZ_User_08 | POD 03-B | https://vc-pod03.hybridlab.local | https://172.18.1.193
DMZ_User_09 | POD 04-A | https://vc-pod04.hybridlab.local | https://172.18.1.197
DMZ_User_10 | POD 04-B | https://vc-pod04.hybridlab.local | https://172.18.1.201
DMZ_User_11 | POD 04-C | https://vc-pod04.hybridlab.local | https://172.18.1.205
DMZ_User_12 | POD 04-D | https://vc-pod04.hybridlab.local | https://172.18.1.209
DMZ_User_13 | POD 06-A | https://vc-pod06.hybridlab.local | https://172.18.1.213
DMZ_User_14 | POD 06-B | https://vc-pod06.hybridlab.local | https://172.18.1.217
DMZ_User_15 | POD 06-C | https://vc-pod06.hybridlab.local | https://172.18.1.221
DMZ_User_16 | POD 06-D | https://vc-pod06.hybridlab.local | https://172.18.1.225
DMZ_User_17 | POD 07-A | https://vc-pod07.hybridlab.local | https://172.18.1.229
DMZ_User_18 | POD 07-B | https://vc-pod07.hybridlab.local | https://172.18.1.233
DMZ_User_19 | POD 07-C | https://vc-pod07.hybridlab.local | https://172.18.1.237
DMZ_User_20 | POD 07-D | https://vc-pod07.hybridlab.local | https://172.18.1.241

### 2.1 Cisco Anyconnect Mobility Client

Run Cisco Anyconnect VPN client available on your desktop.

You’ll need to review and configure the AnyConnect options. After Anyconnect launches, you’ll need to click on the “Configuration” button on the main panel. See image below.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_without_IP.png" width = 500>

In case of the issues with certificate, you will need to uncheck the option that says “Block connections to untrusted servers”. Your selection is immediately saved.

![anyconnect settings picture here](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_settings.png)

Close the Configuration window.

In the main entry field, enter your Private Infrastructure VPN IP Address as provided in the paper sheet on your desk. Then choose “Connect”.

After a few seconds, you’ll see a new window notifying you of an “Untrusted Server Certificate”. This is expected and not a real issue. Choose “Connect Anyway”.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_accept_cert.png" width = 500>

You’ll see a new window prompting you to provide your Lab’s network credentials. Enter the Username and Password as provided in the paper sheet. Choose “OK”.

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_login2.png" width = 500>

Next you’ll see the main AnyConnect window go through several connection states. When it has completed establishing the connection, AnyConnect will iconify in the Notification Area of the Windows Taskbar. When you have an established VPN connection, the AnyConnect icon will display a symbol of a padlock, as shown here.

![Picture of connected VPN icon only](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_icon_connected.png)

Your are connected to infrastructure on-prem. You can interact with resources in your lab by **either using jumphost or accessing devices directly**. 


### 2.2 (Optional) Remote desktop connection

_This step is optional, you can perform all operations from the desktop as well._

Open Remote Desktop Client (icon available on the desktop). If there is no icon for Remote Desktop Connection on the Desktop, click start, and type `mstsc`

Click `show options` and type IP address of the jumphost and username. Don't forget to specify domain name which is `HYBRIDLAB`.

    Computer: 172.18.1.10
    User name: HYBRIDLAB\DMZ_USER_<ID>

Populated fields should be similar to the picture.  

You can find password in the paper sheet or in the `DMZ_USER_XX.txt` file.

**Each user will login to the same jumphost: `172.18.1.10`, regardless of the POD or server they should use**

<img src=https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rdp_dmz_creds.png width = 500>


## 3. Accessing Cisco Container Platform

Cisco Container Platform manages Kuberenetes clusters in the private infrasturcture. You will have access to dedicated instance of Cisco Container Platform, from which you will manage you own Kuberenetes Clusters used later on to deploy application.

Please refer to the [Table 1](LAB_access.md) to access your own Cisco Container Platform dashboad. Use your Active Directory credentials to login without specifying domain name - see following picture:

<img src="https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp_login_ad.png" width = 500>

## 4. Google Cloud access

Open Chrome web browser from your desktop (you can use either jumphost or local PC)
Go to [http://cloud.google.com](https://cloud.google.com), click on sign-in in the top right corner  

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-sign-in.png">

Enter username for your lab pod which you can find in the paper sheet or `DMZ_USER_XX.txt` file on your desktop. You can change language to your preferred.

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-login1.png" width = 500>

Once logged in, click on the `Console` button in the top right corner to open Google Cloud Platform Console.

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-console-button1.png">

When you sign-in to Google Cloud admin panel for the first time, you will be asked to accept Terms of Service, provide country of residence and email updates. Please select following options, and click `AGREE AND CONTINUE`

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-accept-terms1png.png">

Next, you will have to select project - click on the `Select a project`

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-select-project1.png">

In the new window, select project `fwardz-001

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-select-project1-2.png">

Now you can access Google Kubernetes Engine - a Kubernetes Cluster in the Google Cloud

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-go-gke1.png">

You should see screen with warning about no sufficient rights to see the GKE Cluster object, however, you can still navigate to "Workloads" where you can deploy applications on the GKE Cluster.

<img src="https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/images/gcp-gke-workloads1.png">

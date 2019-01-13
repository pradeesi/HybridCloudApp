# Lab Task 1: Connectivity Check

## 1. Lab access general description

The lab has been built leveraging multiple cloud environments as following:

- Amazon Web Services
- Google Cloud
- Private intrastructure on-prem

During this lab, you will get access to Google Cloud and Private Infrastructure, as these are providing container environment. Amazon Web Services is used in this setup as a message broker only to aggregate data from sensors and make it avaialbe to get by application component that you will deploy on-prem in this lab.

Specific user credentials for multiple systems are available in the text file credentials.txt under following link:
**[put here link to cloud drive](https://)**

## 2. On-prem private infrastructure access

In order to get access to private network, please first find credentials for your POD in the file you previously downloaded.

Each server in the private on-premise infrastructure handles multiple Users environment. Single server can have two to four instances of Cisco Container Platform, each dedicated to different User.
For a lab purpose each server is managed by its own vCenter.
Two to four users will share the same hardware server and same vCenter, however each User will have own instance of Cisco Container Platform, which provides Platform as a Service for Kubernetes clusters.
In this lab, Kubernetes clusters are build on to of virtual machines for demonstration purposes.

Below table collects each user lab systems:

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
DMZ_User_15 | POD 06-c | https://vc-pod06.hybridlab.local | https://172.18.1.221
DMZ_User_16 | POD 06-D | https://vc-pod06.hybridlab.local | https://172.18.1.225
DMZ_User_17 | POD 07-A | https://vc-pod07.hybridlab.local | https://172.18.1.229
DMZ_User_18 | POD 07-B | https://vc-pod07.hybridlab.local | https://172.18.1.233
DMZ_User_19 | POD 07-C | https://vc-pod07.hybridlab.local | https://172.18.1.237
DMZ_User_20 | POD 07-D | https://vc-pod07.hybridlab.local | https://172.18.1.241

### 2.1 Cisco Anyconnect Mobility Client

Run Cisco Anyconnect VPN client available on your desktop.

You’ll need to review and configure the AnyConnect options. After Anyconnect launches, you’ll need to click on the “Configuration” button on the main panel. See image below.

![anyconnect_without_IP](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_without_IP.png)

You will need to uncheck the option that says “Block connections to untrusted servers”. Your selection is immediately saved.

![anyconnect settings picture here](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_settings.png)

Close the Configuration window.

In the main entry field, enter your Private Infrastructure VPN IP Address as provided in the credentials.txt. Then choose “Connect”.

After a few seconds, you’ll see a new window notifying you of an “Untrusted Server Certificate”. This is expected and not a real issue. Choose “Connect Anyway”.

![anyconnect picture accept untrusted certificate here](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_accept_cert.png)

You’ll see a new window prompting you to provide your Lab’s network credentials. Enter the Username and Password as provided in the credentials.txt file. Choose “OK”.

![anyconnect picture provide username and password](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_login.png)

Next you’ll see the main AnyConnect window go through several connection states. When it has completed establishing the connection, AnyConnect will iconify in the Notification Area of the Windows Taskbar. When you have an established VPN connection, the AnyConnect icon will display a symbol of a padlock, as shown here.

![Picture of connected VPN icon only](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/anyconnect_icon_connected.png)

**Congratulations!** Your are connected to infrastructure on-prem. You can interact with resources in your lab by either using jumphost or accessing devices directly. 

<!--- does PUTTY is a standard desktop software ? --->

### 2.2 Remote desktop connection

Open Remote Desktop Client (icon available on the desktop) and login to the jumphost which is available under address:

[172.18.0.10](rdp://172.18.0.10)
User your user with a domain HYBRIDLAB\ <user_name>

**![screenshot of remote desktop](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/rdp_dmz_ip.png)**


## 3. Accessing Cisco Container Platrofm

Cisco Container Platform manages Kuberenetes clusters in the private infrasturcture. You will have access to dedicated instance of Cisco Container Platform, from which you will manage you own Kuberenetes Clusters used later on to deploy application.

Please refer to the table 1 to access your own Cisco Container Platform dashboad. Use your Active Directory credentials to login, on the login screen you don't have to specify domain, just type AD username:

**![screenshot of CCP Login page with AD account](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/ccp_login_ad.png)**

## 4. Google Cloud access

Open Chrome web browser from your desktop (you can use either jumphost or local PC)
Go to [http://cloud.google.com](https://cloud.google.com), sign-in using username which you can find in credentials.txt document.

**![screenshot of google login]

This account has access to the Google Kubernetes Engine in Google Cloud. For more information how to navigate in Google Cloud, you can jump to the section:
***[Lab-8 Create Kubernetes Cluster (GKE) on Google Cloud](https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/docs/create_gke_engine.md)***

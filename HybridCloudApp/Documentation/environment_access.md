# Lab-1: Access information

## 1. Lab access general description

The lab has been built leveraging multiple cloud environments as following:

- Amazon Web Services
- Google Cloud
- Private intrastructure on-prem

During this lab, you will get access to Google Cloud and Private Infrastructure, as these are providing container environment. Amazon Web Services is used in this setup as a message broker only to aggregate data from sensors and make it avaialbe to get by application component that you will deploy on-prem in this lab.

Specific user credentials for multiple systems are available in the text file credentials.txt under following link:
**[put here link to cloud drive](https://)**

## 2. On-prem private infrastructure access

In order to get access to private network, please first download credentials for your POD from the following URL:

**[LINK TO BE HERE](https://)**

### 2.1 Cisco Anyconnect Mobility Client

Run Cisco Anyconnect VPN client available on your desktop:

You’ll need to review and configure the AnyConnect options. After Anyconnect launches, you’ll need to click on the “Configuration” button on the main panel. See image below.

**![anyconnect picture here]()**

You will need to uncheck the option that says “Block connections to untrusted servers”. Your selection is immediately saved.

**![anyconnect settings picture here]()**

Close the Configuration window.

In the main entry field, enter your Private Infrastructure VPN IP Address as provided in the credentials.txt. Then choose “Connect”.

**![anyconnect picture with IP address here]()**

After a few seconds, you’ll see a new window notifying you of an “Untrusted Server Certificate”. This is expected and not a real issue. Choose “Connect Anyway”.

**![anyconnect picture accept untrusted certificate here]()**

You’ll see a new window prompting you to provide your Lab’s network credentials. Enter the Username and Password as provided in the credentials.txt file. Choose “OK”.

**![anyconnect picture provide username and password]()**

Next you’ll see the main AnyConnect window go through several connection states. When it has completed establishing the connection, AnyConnect will iconify in the Notification Area of the Windows Taskbar. When you have an established VPN connection, the AnyConnect icon will display a symbol of a padlock, as shown here.

**![Picture of connected VPN icon only]()**

Congratulations! Your are connected to infrastructure on-prem. You can interact with resources in your lab by either using jumphost or accessing devices directly. 

<!--- does PUTTY is a standard desktop software ? --->

### 2.2 Remote desktop connection

Open Remote Desktop Client (icon available on the desktop) and login to the jumphost which is available under address:

[172.18.0.10](rdp://172.18.0.10)
User your user with a domain HYBRIDLAB\ <user_name>

**![screenshot of remote desktop]()**

## 3. Google Cloud access

Open Chrome web browser from your desktop (you can use either jumphost or local PC)
Go to [http://cloud.google.com](https://cloud.google.com), sign-in using username which you can find in credentials.txt document.

**![screenshot of google login]()**

This account has access to the Google Kubernetes Engine in Google Cloud. For more information how to navigate in Google Cloud, you can jump to the section:
***[Lab-8 Create Kubernetes Cluster (GKE) on Google Cloud](https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/Documentation/docs/create_gke_engine.md)***

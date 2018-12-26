# Appendix - 1: AWS IoT Platform Configuration

## 1. What is AWS IoT Platform?
AWS IoT provides broad and deep functionality, spanning the edge to the cloud, so you can build IoT solutions for virtually any use case across a wide range of devices. Since AWS IoT integrates with AI services, you can make devices smarter, even without Internet connectivity. Built on the AWS cloud, used by millions of customers in 190 countries, AWS IoT can easily scale as your device fleet grows and your business requirements evolve. AWS IoT also offers the most comprehensive security features so you can create preventative security policies and respond immediately to potential security issues.


## 2. What Config Do We Need for this Lab?

For this lab we are going to use the MQTT Broker service from AWS IoT Core, which would be used by the IoT Sensor devices (Raspberry Pi with DHT22 sensor in our case) to publish the sensor data.

As the direct MQTT access is not permitted by AWS, we would have to create certificate and policies to allow our sensor devices to publish the sensor data on MQTT Broker. This article would explain the process for the same.

## 3. Prerequisites:

You need to have a valid **AWS Account** with Administrative access to AWS IoT Core.

## 4. Create new MQTT Policies:

Login to **AWS console** and open **AWS IoT Core** page.

### 4.1 Create New Policies:

Click on "**Create**" button on "**Secure --> Policies**" page to create a new policy as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/new_policy.png)

### 4.2 Create MQTT_Connect Policy:

Create a new MQTT_Connect policity with "**iot:Connect**" action, "**\***" Resource ARN and "**Allow**" Effect as shown in the following screenshot - 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/MQTT_Connect.png)

### 4.3 Create MQTT_Publish Policy:

Create a new MQTT_Publish policity with "**iot:Publish**" action, "**\***" Resource ARN and "**Allow**" Effect as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/MQTT_Publish.png)

### 4.4 Create MQTT_Subscribe Policy:

Create a new MQTT_Subscribe policity with "**iot:Subscribe**" action, "**\***" Resource ARN and "**Allow**" Effect as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/MQTT_Subscribe.png)

### 4.4 Check the Policies Page:

Your **Policies** page should look similar to the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/new_policies_final.png)

## 5. Create new Certificate and Associate Policies With It:

### 5.1 Create New Policies:

Click on "**Create**" button on "**Secure --> Certificates**" page to create a new certificate as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/new_policy.png)
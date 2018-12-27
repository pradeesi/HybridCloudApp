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

Click on the "**Create**" button on "**Secure --> Policies**" page to create a new policy as shown in the following screenshot -

**Note:** If you are creating a Policy for the first time, you may see a different screen with "**Create a policy**" button. Just click on that button and follow other steps.

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

## 5. Create and Download new Certificate:

### 5.1 Create New Policies:

Click on the "**Create**" button on "**Secure --> Certificates**" page to create a new certificate as shown in the following screenshot -

**Note:** If you are creating a Certificate for the first time, you may see a different screen with "**Create a certificate**" button. Just click on that button and follow other steps.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/new_certificate.png)

### 5.2 Create One-Click-Certificate:

Click on the "**Create certificate**" button to create a new One-click-certificate as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/one-click-certificate.png)

### 5.3 Download Certificates:

Click on the "**Download**" buttons and download the Certificate file, Public key, and Private key file as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/Download_cert.png)

### 5.4 Close the Create Certificate Page:

Close the "Create Certificate" page by clicking on the "**Done**" button.

### 5.4 Download Amazon Root CA Certificate:

Save the "**RSA 2048 bit key: Amazon Root CA 1**" file from the following page as "**AmazonRootCA.crt**" -

(Page URL - [https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html#server-authentication](https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html#server-authentication))

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/AWS_Root_CA.png)

### 5.5 Check the Certificates Page:

Now on the "**Secure --> Certificates**" page you should see a new certificate. Note that your certificate is still inactive.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/certificate_page.png)

## 6. Activate the Certificate:

Navigate to "**Secure --> Certificates**"; click on the Certificate options and select "**Activate**" to activate the certificate as shown in following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/activate_certificate.png)

## 7. Associate the Policies with Certificate:

Navigate to "**Secure --> Certificates**" and click on the certificate to modify the certificate properties. On this certificate properties page click on "**Policies**" and from the "**Actions**" menu select "**Attach Policy**" as shown in the following screenshot - 

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/Attach_Policies.png)

Select all the policies and click on "**Attach**" button as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/select_policies.png)

Your certificate Policies section should look like this -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/certificate_policies.png)

## 8. Locate Custom Endpoint:

You would need Custom endpoint to connect to the AWS IoT platform. It will be used by the MQTT clients as MQTT Broker host. You can locate your Customer Endpoint under "Settings" section as shown in the following screenshot -

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/custom_endpoint.png)






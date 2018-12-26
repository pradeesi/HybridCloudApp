# Appendix - 1: AWS IoT Platform Configuration

## 1. What is AWS IoT Platform?
AWS IoT provides broad and deep functionality, spanning the edge to the cloud, so you can build IoT solutions for virtually any use case across a wide range of devices. Since AWS IoT integrates with AI services, you can make devices smarter, even without Internet connectivity. Built on the AWS cloud, used by millions of customers in 190 countries, AWS IoT can easily scale as your device fleet grows and your business requirements evolve. AWS IoT also offers the most comprehensive security features so you can create preventative security policies and respond immediately to potential security issues.


## 2. What Config Do We Need for this Lab?

For this lab we are going to use the MQTT Broker service from AWS IoT Core, which would be used by the IoT Sensor devices (Raspberry Pi with DHT22 sensor in our case) to publish the sensor data.

As the direct MQTT access is not permitted by AWS, we would have to create certificate and policies to allow our sensor devices to publish the sensor data on MQTT Broker. This article would explain the process for the same.

## 3. Prerequisites:

You need to have a valid **AWS Account** with Administrative access to AWS IoT Core.




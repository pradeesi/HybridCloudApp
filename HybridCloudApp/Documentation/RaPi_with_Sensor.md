# Appendix - 1
## Raspberry Pi with DHT22 Humidity and Temperature Sensor


## 1. Hardware and Software Components:
Following are the Hardware and Software prerequisites that you need before you begin with this article - 

### 1.1 Hardware Components:
* Raspberry Pi with Power Adapter
* SD Card and SD Card Reader
* DHT22 Sensor
* 10K Ohm Resistor
* Jumper wires and Breadboard
* Keyboard and Monitor (Optional)

### 1.2 Software Components:
* [Official Raspbian Image](https://www.raspberrypi.org/downloads/raspbian/)
* [Etcher] (https://www.balena.io/etcher/) for flashing Raspbian OS image into theSD card

## 2. DHT22 Sensor Connection with Raspberry Pi
You can connect the DHT22 sensor with Raspberry Pi as shown in the following image. Pin 1 and Pin 4 on the sensor should be connected to the 3.3V Power Pin and Ground Pin respectively. Pin 2 on the sensor should be connected to GPIO Pin 4.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/Rapi_sensor_connection.png)

## 3. Burn Raspbian OS on the SD Card and enable SSH
Use [Etcher] (https://www.balena.io/etcher/) to install the Raspbian OS on the SD card.

For headless setup, SSH can be enabled by placing a file named ssh, without any extension, onto the boot partition of the SD card from another computer. When the Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all.

If you have loaded Raspbian onto a blank SD card, you will have two partitions. The first one, which is the smaller one, is the boot partition. Place the file into this one.

## 4. Install Docker Runtime


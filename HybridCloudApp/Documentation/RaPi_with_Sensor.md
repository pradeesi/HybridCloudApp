# Appendix - 1: Raspberry Pi with DHT22 Humidity and Temperature Sensor


## 1. Hardware and Software Components:
Following are the Hardware and Software prerequisites that you need before you begin with this article - 

### 1.1 Hardware Components:
* Raspberry Pi with Power Adapter
* SD Card and SD Card Reader
* Ethernet Cable
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
Download the [Rasbian](https://www.raspberrypi.org/downloads/raspbian/) OS and use [Etcher] (https://www.balena.io/etcher/) to install it on the SD card. For headless setup, open the SD Card on your computer, after the installation process gets completed to enable SSH.

SSH can be enabled by placing a file named ssh, without any extension, onto the boot partition of the SD card from another computer. When the Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all.

If you have loaded Raspbian onto a blank SD card, you will have two partitions. The first one, which is the smaller one, is the boot partition. Place the file into this one.

Now plug the SD card into your Raspberry Pi and power it on.

## 4. SSH into the Raspberry Pi and Install Docker Runtime
SSH into your Raspberry Pi using the following command (replace <ip-address> with the IP Address assigned to your raspberry Pi) -

	ssh pi@<ip address>
	
On the password prompt you could use the default raspberry password - "**raspberry**"

Now you should have access to the shell. Upgrade raspbian packages using the following command - 

	sudo apt-get update && sudo apt-get upgrade
	
Install Docker runtime using the following command -

	curl -sSL https://get.docker.com | sh
	
Add permission to Pi user to run Docker commands by adding “pi” user to “docker” group using the following command –

	sudo usermod -aG docker pi
	
You must Log off from Raspberry Pi and Login again, for this to take effect.

Check Docker installation using the following command -

	docker --version

If you see the correct version, you are good to go.

## 5. Download Required Files and Upload on Raspberry Pi:

**5.1** Download the Certificate files from from AWS IoT core as described in Appendix 1

**5.2** Download the "**settings.ini**" from github repo - [Link](https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/RaspberryPi/settings.ini)

**5.3** Update the settings file variables accordingly.

**5.4** Login to Raspberry Pi and create new settings folder under the 'pi' user's home directory, using the following command - 

	mkdir settings
	
**5.5** Upload the AWS Certificate Files and updated "settings.ini" file on Raspberry Pi using sftp -

	sftp pi@<ip-address>

	cd settings

	put <file-name>

## 6. Configure Raspberry Pi to Trigger the IoT Container:
 



	








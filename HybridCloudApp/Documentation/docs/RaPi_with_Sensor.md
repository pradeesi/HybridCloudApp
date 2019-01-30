# Appendix - 2: Raspberry Pi with DHT22 Sensor and Docker Container


## 1. Hardware and Software Requirements:
Following are the Hardware and Software prerequisites that you need before you begin with this article - 

### 1.1 Hardware:
* Raspberry Pi with Power Adapter
* SD Card and SD Card Reader
* Ethernet Cable
* DHT22 Sensor
* 10K Ohm Resistor
* Jumper wires and Breadboard
* Keyboard and Monitor (Optional)

### 1.2 Software:
* [Official Raspbian Image](https://www.raspberrypi.org/downloads/raspbian/)
* [Etcher](https://www.balena.io/etcher/) for flashing Raspbian OS image into theSD card

## 2. DHT22 Sensor Connection with Raspberry Pi
You can connect the DHT22 sensor with Raspberry Pi as shown in the following image. Pin 1 and Pin 4 on the sensor should be connected to the 3.3V Power Pin and Ground Pin respectively. Pin 2 on the sensor should be connected to GPIO Pin 4.

![Rapi](https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Documentation/images/Rapi_sensor_connection.png)

## 3. Burn Raspbian OS on the SD Card and enable SSH
Download the [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) OS and use [Etcher] (https://www.balena.io/etcher/) to install it on the SD card. For headless setup, open the SD Card on your computer, after the installation process gets completed to enable SSH.

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

**5.1** Download the Certificate files from from AWS IoT core as described in Appendix - 1

**5.2** Download the "**settings.ini**" from github repo - [Link](https://github.com/pradeesi/HybridCloudApp/blob/master/HybridCloudApp/RaspberryPi/settings.ini)

**5.3** Update the settings file variables accordingly.

**5.4** Login to Raspberry Pi and create new settings folder under the 'pi' user's home directory, using the following command - 

	mkdir /home/pi/settings
	
**5.5** Upload the AWS Certificate Files and updated "settings.ini" file on Raspberry Pi using sftp -

	sftp pi@<ip-address>

	cd /home/pi/settings

	put <file-name>
	
**Note:** Make sure you copy the updated settings.ini, Amazon RootCA Certificate file, AWS IoT Core Things Certificate & Private Key files into the '/home/pi/settings' directory on your Raspberry Pi.

**5.6** Close the sftp session using the following command -

	bye

## 6. Test the Container on Raspberry Pi:

Login back into the Raspberry Pi and run the sensor container in an interactive mode using the following command -

	sudo docker run --privileged -it -v /home/pi/settings:/usr/src/app/settings pradeesi/rapi_cl_hc_sensor


## 7. Configure Raspberry Pi to Trigger the Sensor Container at Startup:
**7.1** open the 'rc.local' using the following command -

	sudo vi /etc/rc.local
	
**7.2** Add following command at the top of this file (preferably in the first line) - 

	sudo docker run --privileged -d -v /home/pi/settings:/usr/src/app/settings pradeesi/rapi_cl_hc_sensor
	
**7.3** Save the file using '**Esc + :wq**' command on vi editor.

**7.4** Change the execution bit using the following command -

	sudo chmod +x /etc/rc.local

**7.5** Reboot the Raspberry Pi using '**sudo reboot**'. 

**7.6** After the reboot process gets completed, login back to the Raspberry Pi and check if the sensor container is running using the command '**sudo docker ps**'.

**Note:** If the docker container is not getting triggered on system startup, add 5 second delay by adding '**sleep 5**' before the docker command added in the 'rc.local' file (in Step# 7.2).






# Explore Backend App and Kubernetes Dashboard:

Your Hybrid Cloud App's backend compoents (MariaDB, MQTT DB Agent, and REST API agent) should be up and running. Now let's explore some low level details to understand the application containers and kubernetes better.

**Task 1:** Find the size of the 'Persistent Volume Claim' used for MariaDB database?

1. Execute '**kubectl get pvc mariadb-pv-claim**' on kubernetes master node and check 'CAPACITY' value.

**Task 2:** Check if the 'MQTT to DB Agent' is receiving data from AWS IoT. (Hint: check the logs in 'MQTT to DB Agent' Pod)

1. Find the pod name for 'MQTT to DB Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mqtt-db-agent-'
1. Check the container logs using the kubectl command '**kubectl logs \<pod name\>**' (replace the pod name with correct value). You should see the Json messages received from AWS IoT platform.


**Task 3:** Assuming that the 'MQTT to DB Agent' connects to the AWS IoT Core on port '8883' and to MariaDB on port '3306'; connect with the 'iot-backend-mqtt-db-agent' pod and check the active connections.

1. Find the pod name for 'MQTT to DB Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mqtt-db-agent-'.
2. login to the container using the kubectl command '**kubectl exec -it \<pod name\> /bin/ash**' (replace the pod name with correct value).
3. On the container shell execute the command '**netstat -n**' and check the 'Foreign Address' column. Look for port number '8883' and '3306'.
4. Exit the container shell using '**exit**' command.

**Task 4:** Login to the MariaDB database and explore the data tables. 

1. Find the pod name for 'MariaDB' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mariadb-'.
2. login to the MariaDB container using the kubectl command '**kubectl exec -it \<pod name\> /bin/bash**' (replace the pod name with correct value).
3. Execute '**ss -tulpn**' and check the port MariaDB is listing to for incoming connections.
4. You can also check the version of MariaDB using the shell command '**mysql --version**'
4. Now connect to the MariaDB from the container shell and check Databases and Tables. Use '**mysql -u root -pcisco123**' command to login to MaraDB.
5. On mariaDB shell, use '**show databases;**' command to list all the databases. Look for '**sensor\_db**' in the output (this is the database where we are storing the sensor data).
6. Switch to sensor_db using the command '**use sensor\_db;**' and list all the tables in this database using the command '**show tables;**'. You should see only one table with the name 'sensor\_data';
7. Try to list the data from this table using the SQL statement **'select * from sensor\_data;**'.
8. Now check the record count in this table using the '**select count\(\*\) from sensor\_data;**' sql statement.
9. Repeat the SQL from step 8 several times and check if the record count is increasing (each sensor would send the data after every 10 seconds). 
10. Use '**exit**' command at MariaDB prompt to exit the DB shell.
11. Use '**exit**' command again to exit 'iot-backend-mariadb' container shell.


**Task 5:** Connect to the REST API Agent container and find the port it is listing on for incoming REST calls.

1. Find the pod name for 'REST API Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-rest-api-agent-' (you may see more than one pod for this service, pick any one).
2. login to the REST API Agent container using the kubectl command '**kubectl exec -it \<pod name\> /bin/ash**' (replace the pod name with correct value).
3. Execute '**netstat -an**' command on the container shell and check the output. This container listens on port '5050' for incoming REST connections and connects with MariaDB using port '3306' (Connection to DB will timeout in case there are no requests coming in).
4. Use '**exit**' command to come out of the container shell.


**Task 6:** Check the logs messages from 'REST API Agent'.

1. Find the pod name for 'REST API Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-rest-api-agent-' (you may see more than one pod for this service, pick any one).
2. check the logs using the kubectl command '**kubectl logs \<pod name\>**'


**Task 7:** How the traffic would be distributed, if you have multiple Kubernetes Pods behind a Kubernetes NodePort Service?

1. Right click on top of your putty window and click on "Duplicate Session" (You should have two putty windows side by side logged into same kubernetes master node).
2. In the first putty window (logged into kubernetes master) execute the command '**kubectl get nodes -o**' and note down the Kubernetes master node's external IP address.
4. Open a web browser on your machine and access the following url (add the master node ip in the url) -
		
		http://<kubernetes node's external ip>:30500/temperature

5. In the first putty window, run '**kubectl get pods**' on the Kubernetes Master. In the output you should see 2 pods for 'iot-backend-rest-api-agent'.
6. In the first putty window, run the command '**watch kubectl logs \<first pod name\>**' (Use the first 'iot-backend-rest-api-agent' pod out of 2 pods that you saw in the output of the command executed in step#5).
7. In the Second putty window, display the logs for second 'iot-backend-rest-api-agent' pod using the command '**watch kubectl logs \<second pod name\>**'.
8. Refresh or reload the web page	 with the url you used in step 4. 
9. Repeat step 8 and check the requests hitting the kubernetes pods in the log messages.


**Task 8:** Login to Kubernetes Dashboard and explore the Backend App components.

**Kubernetes Dashboard \> Nodes**: You would see the Kubernetes Cluster Nodes on this screen.

**Kubernetes Dashboard \> Persistent volume**: You should see all the persistent values. Try to locate the persistent volume created for MariaDB.

**Kubernetes Dashboard \> Overview \> Workloads \> deployments**: You should see all the app components with the number of pods for each deployment.

**Kubernetes Dashboard \> Overview \> Workloads \> pods**: On this screen you should see all the pods for your application.

**Kubernetes Dashboard \> Overview \> Workloads \> Replica Set**: Click on a deployment name to view the detaild of Pods and Containers. 

**Kubernetes Dashboard \> Overview \> Workloads \> Replica Set**: Click on a Logs icon on right hand side to view the container logs.

**Kubernetes Dashboard \> Discovery and Load Balancing \> Services**: On this screen you would see list of Kubernetes Services deployed on your cluster.

**Kubernetes Dashboard \> Config and Storage \> Secrets**: This screen would show the secret created for MariaDB.









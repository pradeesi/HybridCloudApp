**Task 1:** Find the size of the 'Persistent Volume Claim' used for MariaDB database?

1. Execute '**kubectl get pvc mariadb-pv-claim**' on kubernetes master node and check 'CAPACITY' value.


**Task 2:** Check if the 'MQTT to DB Agent' is recieving data from AWS IoT. (Hint: check the logs in 'MQTT to DB Agent' Pod)

1. Find the pod name for 'MQTT to DB Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mqtt-db-agent-'
2.  Check the container logs using the kubectl command '**kubectl logs \<pod name\>**' (replace the pod name with correct value). You should see the Json messages recieved from AWS IoT platform.


**Task 3:** Assuming that the 'MQTT to DB Agent' connects to the AWS IoT Core on port '8883' and to MariaDB on port '3306'; connect with the 'iot-backend-mqtt-db-agent' pod and check the active connections.

1. Find the pod name for 'MQTT to DB Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mqtt-db-agent-'.
2. login to the container using the kubectl command '**kubectl exec -it \<pod name\> /bin/ash**' (replace the pod name with correct value).
3. On the container shell execute the command '**netstat**' and check the 'Foreign Address' column. Look for port number '8883' and '3306'.
4. Exit the container shell using '**exit**' command.

**Task 4:** Login to the MariaDB database and explore the data tables. 

1. Find the pod name for 'MariaDB' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-mariadb-'.
2. login to the MariaDB container using the kubectl command '**kubectl exec -it \<pod name\> /bin/bash**' (replace the pod name with correct value).
3. Execute '**ss -tulpn**' and check the port MariaDB is listing to for incomming connections.
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
3. Execute '**netstat -an**' command on the container shell and check the output. This container listens on port '5050' for incomming REST connections and connects with MariaDB using port '3306' (Connection to DB will timeout in case there are no requests coming in).
4. Use '**exit**' command to come out of the container shell.


**Task 6:** Check the logs messages from 'REST API Agent'.

1. Find the pod name for 'REST API Agent' using the kubectl command '**kubectl get pods**' and locate the pod name starting with 'iot-backend-rest-api-agent-' (you may see more than one pod for this service, pick any one).
2. check the logs using the kubectl command '**kubectl logs \<pod name\>**'
3. **\(Optional\)** This is an optional step. If you have 2 pods for 'REST API Agent', open two ssh session to your kubernetes master and check the logs for both pods in two different windows. After this try to access some REST calls repeatedly and check if the NodePort service is doing some load balancing towards your Pods?












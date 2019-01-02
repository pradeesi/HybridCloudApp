
### Create Kubernetes Secret:

* **Create DB Password Secret:**

		kubectl create secret generic mariadb-root-pass --from-literal=password=cisco123

* **Verify DB Password Secret:**

		kubectl get secrets

### Create PersistentVolume:

* **Create Persistent Volume:** 

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Frontend/Mariadb/mariadb_persistent_volume.yaml

* **Verfiy PersistentVolume:**

		kubectl get pvc
	
	**Note:** It can take up to a few minutes for the PVs to be provisioned.
	
### Deploy Database:

* **Deploy MariaDB:**

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Frontend/Mariadb/mariadb_deployment.yaml
		
* **Check Deployment Status:**

		kubectl get deployment
		




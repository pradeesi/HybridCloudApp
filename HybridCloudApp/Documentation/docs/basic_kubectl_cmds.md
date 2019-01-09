
kubectl version


kubectl get nodes

kubectl run <deployment_name> --image=<container_image> --port=<port>


### Kubernetes Deployments:
A Deployment controller provides declarative updates for Pods and ReplicaSets. 

You describe a desired state in a Deployment object, and the Deployment controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

* **Create Deployment** Use the following command to create a deployment using a yaml file -

		kubectl create -f <yaml file path>

* **List Deployments:** Use the following command to list all kubernetes deployments -

		kubectl get deployments

* **Deployment Details:** Use the following command to display the details of deployment - 

		kubectl describe deployment
	
* **Scale Deployment:** Use the following command to scale (up/down) a kubernetes deployment -

		kubectl scale deployments/<deployment_name> --replicas=<number of replicas>

* **Delete Deployment:** Use the following command to delete a deployment -

		kubectl delete deployment <deployment_name>


### Kubernetes Pods:
A Pod represents a unit of deployment: a single instance of an application in Kubernetes, which might consist of either a single container or a small number of containers that are tightly coupled and that share resources.

* **List Pods:** Use the following command to list all the pods:

		kubectl get pods
	
	or use wide option to see more details -
	
		kubectl get pods -o wide	

* **List Pods Filter:** You can filter the pods using the labels used in deployment -

		kubectl get pods -l <label_name>=<label_value>


* **Pod Details:** Use the following command to see the containers and used images for pods -

		kubectl describe pods

* **Pod Logs:** Use the following command to check the pod logs -

		kubectl logs <pod_name>


### Kubernetes Services:

A Kubernetes Service is an abstraction which defines a logical set of Pods and a policy by which to access them - sometimes called a micro-service.

* **List Service:** Use the following command to list the current Services -

		kubectl get services

	You can filter the services using the labels used in deployment -

		kubectl get services -l <label_name>=<label_value>

* **Create Service:** Use the following command to create a new service -

		kubectl expose deployment/<deployment_name> --type="NodePort" --port <port>

* **Service Details:** Use the following command to find out what port was opened externally (by the NodePort option) -

		kubectl describe services/<service_name>
	
* **Delete Service:** Use the following command to delete a service -

		kubectl delete service/<service_name>
or

		kubectl delete service -l <label_name>=<label_value>
	

* **Parse Service Node Port:** Use the following script to filterout the node-port of a service (change the service name) -

		export NODE_PORT=$(kubectl get services/<service-name> -o go-template='{{(index .spec.ports 0).nodePort}}')
	
		echo NODE_PORT=$NODE_PORT


### Kubernetes Secrets:

A Secret is an object that stores a piece of sensitive data like a password or key.

* **List Secrets:** Use the following command to list all secrets

		kubectl get secrets
		
* **Secret Details:** Use the following command to list the secret details - 

		kubectl describe secrets/<secret_name>

* **Create Secret:** Use the following command to create secret -

		kubectl create secret generic <secret_name> --from-literal=<key_name>=<key_value>

* **Delete Secret:** use the following command to delete a secret - 
		
		kubectl delete secret <secret_name>


### Interacting with Pod Containers

* **List Env Variables:** Use the following command to list the environment variables -

		kubectl exec <pod_name> env
	
* **Access Container Shell:** Use the following command to access bash shell in a container - 
	
		kubectl exec -ti <pod_name> bash
	
	**Note:** To close your container connection type '**exit**'.


###=========================================

kubectl proxy

curl http://localhost:8001/version

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME


curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy

=========================================



# Applying Kubernetes Network Policies to Secure the Application

A network policy is a specification of how groups of pods are allowed to communicate with each other and other network endpoints.

NetworkPolicy resources use labels to select pods and define rules which specify what traffic is allowed to the selected pods.

By now you should have your Hybrid Cloud IoT Application working end to end. Let's apply some Kubernetes Network Policies to allow traffic from the frontend app to port '5050' only (REST API AGENT container accepts HTTP requests on port '5050').

## 1. Apply Deny All Network Policy:

Following Kubernetes Network Policy yaml definition would block all the traffic coming towards REST API Agent -

	apiVersion: networking.k8s.io/v1
	kind: NetworkPolicy
	metadata:
	  name: deny-all-rest-api-agent
	spec:
	  podSelector:
	    matchLabels:
	      app: iot-backend-rest-api-agent
	      tier: rest-api-agent
	  policyTypes:
	  - Ingress

* 1.0: Prerequisite - set `kubectl` context to `on-prem-1` and make sure that your default namespace is set to your student ID.

		kubectl config use-context on-prem-1
		kubectl config get-contexts

> Note: if you notice that the `Namespace` column contains wrong or none Namespace please update it using folloowing command 

		kubectl config set-context on-prem-1 --namespace studentXX ## where XX is your student ID.

* 1.1: Execute the following command on Kubernetes master node to apply this Network Policy on your REST API Agent -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Network_Policies/deny_all_rest_api_agent.yaml
	
* 1.2: Now try to referesh your Frontend App webpage. It should stop working.


## 2. Apply Permit Port 5111 Network Policy:

Following Kubernetes Network Policy yaml definition would allow the traffic on port 5111 to REST API Agent -

	apiVersion: networking.k8s.io/v1
	kind: NetworkPolicy
	metadata:
	  name: permit-port-5111-rest-api-agent
	spec:
	  podSelector:
	    matchLabels:
	      app: iot-backend-rest-api-agent
	      tier: rest-api-agent
	  policyTypes:
	  - Ingress
	  ingress:
	  - from: []
	    ports:
	    - protocol: TCP
	      port: 5111

* 2.1: Execute the following command on Kubernetes master node to apply this Network Policy on your REST API Agent -

	 	kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Network_Policies/permit_port_5111_rest_api_agent.yaml
	 	

* 2.2: Now try to referesh your Frontend App webpage. **Does it work? Why?**


## 3. Apply Permit Port 5050 Network Policy:

Following Kubernetes Network Policy yaml definition would allow the traffic on port 5050 to REST API Agent -

	apiVersion: networking.k8s.io/v1
	kind: NetworkPolicy
	metadata:
	  name: permit-port-5050-rest-api-agent
	spec:
	  podSelector:
	    matchLabels:
	      app: iot-backend-rest-api-agent
	      tier: rest-api-agent
	  policyTypes:
	  - Ingress
	  ingress:
	  - from: []
	    ports:
	    - protocol: TCP
	      port: 5050
	      
* 3.1: Execute the following command on Kubernetes master node to apply this Network Policy on your REST API Agent -

		kubectl create -f https://raw.githubusercontent.com/pradeesi/HybridCloudApp/master/HybridCloudApp/Kubernetes/Backend/Network_Policies/permit_port_5050_rest_api_agent.yaml
		
* 3.2: Now try to referesh your Frontend App webpage. **Does it work? Why?**


> **Note: Other command related to Network Policy that you may use -
**

* Display Kubernetes Network Policies -
	
 		kubectl get NetworkPolicies
 	
* Display Network Policy Details -
 
	 	kubectl describe NetworkPolicy <Network Policy Name>

* Delete Network Policy -
 
	 	kubectl delete NetworkPolicy <Network Policy Name>
Steps for Helm Chart:

Before executing helm, delete all the running resources or helm will complain about resource already existing.
1. To delete everything in a namespace
`kubectl delete all --all -n default`

2. `helm install surveyapp-release surveyapp-helm/` 
		
3. To check whether helm worked:
    `Kubectl get all`
    - this should display all the resources  
   ` Minikube tunnel`
    - to tunnel the loadbalancer and then check surveyapp.com on browser

4. After updating anything in values.yaml, this command needs to be executed in the home directory:
    `helm upgrade surveyapp-release surveyapp-helm/ --values surveyapp-helm/values.yaml`
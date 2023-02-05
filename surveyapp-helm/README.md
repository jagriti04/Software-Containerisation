# Steps for Helm Chart:

1. To create - `kubectl helm create surveyapp-helm`

    Before executing helm, delete all the running resources or helm will complain about resource already existing.
    To delete everything in a namespace
    `kubectl delete all --all -n default`
    also delete hpa, pv, pvc, secrets.

    Or if helm is already installed do, `helm ls` then `helm uninstall surveyapp-release`

2. `kubectl helm install surveyapp-release surveyapp-helm/` 
    - the release name here is unique 
		
3. To check whether helm worked:
    `Kubectl get all`
    - this should display all the resources  
   ` Minikube tunnel`
    - to tunnel the loadbalancer and then check surveyapp.com on browser

4. To deploy the helm or after updating anything in values.yaml, this command needs to be executed in the home directory:
    `helm upgrade surveyapp-release surveyapp-helm/ --values surveyapp-helm/values.yaml`

5. To see the current applied helm - `helm ls`
    - this would list the application with the release number specified while creating the helm chart.
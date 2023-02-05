---------------------------------------------------
## Microk8s installation
---------------------------------------------------
1. check if microk8s is installed <br />
    -> `microk8s status`

2. check mircok8s add-ons <br />
    -> `microk8s status` (look for)
    ```
        --> dashboard
        --> dns
        --> helm (heml3)
        --> hostpath-storage
        --> ingress
        --> rbac
        --> registry
        --> storage
    ```
---------------------------------------------------
## Paths
---------------------------------------------------
3. create storage paths 
```
    -> /var/lib/postgresql/data
    -> /mnt/data
```
---------------------------------------------------
## Local docker images
---------------------------------------------------
4. create the frontend & restapi images locally <br />
    -> `docker-compose build`

5. port the images to microk8s <br />
    -> `sudo docker save [image name] > [image name].tar` <br />
    -> `sudo microk8s ctr image import [image name].tar`

6. check if images are in locall registry <br />
    -> `microk8s ctr images list` (look for REF) <br />
        --> docker.io/library/frontend:latest <br />
        --> docker.io/library/restapi:latest

---------------------------------------------------
## CERT-manager
---------------------------------------------------
7. install cert-manager <br />
    ->  `kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.11.0/cert-manager.yaml`

---------------------------------------------------
## GCP
---------------------------------------------------
8. gcp artifcat registry create/ update<br />
    -> `sudo docker tag [image-name] europe-west4-docker.pkg.dev/sc-32-376820/survey-app/[image-name]:tag`

9. gcp push image<br />
    -> `docker push europe-west4-docker.pkg.dev/sc-32-376820/survey-app/[image-name]:tag`

10. create gcp compatible helm chart<br />
    -> `helm package .\surveyapp-helm\`

11. push compiled helm chart to gcp
    -> `helm push surveyapp-helm-0.1.1.tgz oci://europe-west4-docker.pkg.dev/sc-32-376820/survey-app`

12. run the helm chart
    -> `helm install [release-name] oci://europe-west4-docker.pkg.dev/sc-32-376820/survey-app/surveyapp-helm --version 0.1.1`

---------------------------------------------------
## Local helm chart
---------------------------------------------------
13. run the helm chart <br />
    -> `sudo microk8s helm3 install [name] ./surveyapp-helm`

14. test role based access <br />
    -> `kubectl auth can-i get pod --namespace default --as sc`

---------------------------------------------------
## Database migration
---------------------------------------------------
15. find the restapi pod name <br />
    -> `kubectl get pods` (look for) <br />
        --> restapi-deployment-[hash]

16. connect to restapi pod <br />
    -> `kubectl exec -it restapi-deployment-[hash] /bin/bash`

17. migrate database to postgresql (inside pod terminal starts with #) <br />
    -> `python manage.py migrate`

18. exit pod terminal <br />
    -> Ctrl + P

---------------------------------------------------
## Operational
---------------------------------------------------

19. check the port for the frontend <br />
    -> `kubectl get svc `(look for) <br />
        --> frontend-service (e.g., 4200:32478/TCP -> localhost:32478 is the IP)

20. open a browser

15. enter URL: localhost:[port] (e.g., localhost:32478)

---------------------------------------------------
## Uninstalling
---------------------------------------------------
21. uninstall helm chart <br />
    -> `sudo microk8s helm3 delete $(microk8s helm3 list --short)`

22. unistall specific chart <br />
    -> `helm uninstall [release-name]`
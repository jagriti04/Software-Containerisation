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
## Helm chart
---------------------------------------------------
7. run the helm chart <br />
    -> `sudo microk8s helm3 install [name] ./surveyapp-helm`

---------------------------------------------------
## Database migration
---------------------------------------------------
8. find the restapi pod name <br />
    -> `kubectl get pods` (look for) <br />
        --> restapi-deployment-[hash]

9. connect to restapi pod <br />
    -> `kubectl exec -it restapi-deployment-[hash] /bin/bash`

10. migrate database to postgresql (inside pod terminal starts with #) <br />
    -> `python manage.py migrate`

---------------------------------------------------
## Operational
---------------------------------------------------
11. exit pod terminal <br />
    -> Ctrl + P

12. check the port for the frontend <br />
    -> `kubectl get svc `(look for) <br />
        --> frontend-service (e.g., 4200:32478/TCP -> localhost:32478 is the IP)

13. open a browser

14. enter URL: localhost:[port] (e.g., localhost:32478)

---------------------------------------------------
## Uninstalling
---------------------------------------------------
15. uninstall helm chart <br />
    -> `sudo microk8s helm3 delete $(microk8s helm3 list --short)`
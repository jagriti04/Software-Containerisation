<!-- # SurveyApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 15.1.1.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.



---------------------------------------------------
## Docker Configuration
---------------------------------------------------

Steps to setup the containers:

1. Navigate to the root folder of the repository, which looks like:
```
Project folder/
---- Rest-API
---- Frontend
---- db
---- ...
```

2. Once here, you can run the following commands:
`docker-compose up -d --build`
// -d is detached mode, so terminal doesn't get locked.

3. For getting the backend working, you'll need to run migrations inside the container, you can open a bash terminal to the container by running

`docker-compose exec <service-name> bash`
e.g. docker-compose exec restapi bash

Once inside there you can run the commands you usually would run.
`python manage.py migrate`

4. Then run `docker-compose ps` to make sure all three containers are up.

5. To check on the browser -
    For Restapis, go to - localhost:8000/survey/home, that should give a hello message.
    For Database, make a curl request from terminal - `curl localhost:5432`, that should say 'empty server response'
    For Frontend, go to - `localhost:4200` that should give the minimal UI we have  -->

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

8. test role based access <br />
    -> `kubectl auth can-i get pod --namespace default --as sc`

---------------------------------------------------
## Database migration
---------------------------------------------------
9. find the restapi pod name <br />
    -> `kubectl get pods` (look for) <br />
        --> restapi-deployment-[hash]

10. connect to restapi pod <br />
    -> `kubectl exec -it restapi-deployment-[hash] /bin/bash`

11. migrate database to postgresql (inside pod terminal starts with #) <br />
    -> `python manage.py migrate`

---------------------------------------------------
## Operational
---------------------------------------------------
12. exit pod terminal <br />
    -> Ctrl + P

13. check the port for the frontend <br />
    -> `kubectl get svc `(look for) <br />
        --> frontend-service (e.g., 4200:32478/TCP -> localhost:32478 is the IP)

14. open a browser

15. enter URL: localhost:[port] (e.g., localhost:32478)

---------------------------------------------------
## Uninstalling
---------------------------------------------------
16. uninstall helm chart <br />
    -> `sudo microk8s helm3 delete $(microk8s helm3 list --short)`
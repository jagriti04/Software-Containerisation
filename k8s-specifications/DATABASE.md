INSTALLATION
1. 'kubectl apply -f postgres-secrets.yaml' 

2. 'kubectl apply -f pv.yaml' 

3. 'kubectl apply -f pvc.yaml' 

4. 'kubectl apply -f postgres-deployment.yaml' 

5. 'kubectl apply -f postgres-service.yaml'

INTERACTION
6. 'kubectl get service postgres'

NAME       TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE

postgres   NodePort   10.108.161.74   <none>        5432:30617/TCP   17m

Look for secondary number in PORT(S) e.g.30617. This is the port you can connect to with: <Cluster IP>:<Node port>

7. Connect to you database, with your set password, and username
1. Run "microk8s enable rbac" || "minikube start --extra-config=apiserver.Authorization.Mode=RBAC"

2. Run "kubectl apply -f pod-reader.yaml"

3. Run "kubectl apply -f pod-reader-binding.yaml"

Test
4. Run "kubectl auth can-i get pod --namespace default --as sc"
--> If "yes" binding and reader are working

5. Run "kubectl apply -f secret-reader.yaml"

6. Run "kubectl apply -f secret-reader-binding.yaml"
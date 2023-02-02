sudo microk8s helm3 install survey ./surveyapp-helm
sudo microk8s helm3 delete $(microk8s helm3 list --short)

sudo docker-compose build
sudo docker save restapi > restapi.tar
m ctr image import restapi.tar
-> m == microk8s

k get svc
-> k == microk8s kubectl

README FOR DATABASE MIGRATION
For installing GCP:
1. Creat account on GCP
2. `cd ~`
`./google-cloud-sdk/install.sh`
`source ~/.bash_profile`
`gcloud init`
` gcloud components install gke-gcloud-auth-plugin`

`gcloud container clusters get-credentials cluster-1`

`gcloud auth configure-docker`

3. switch to docker-compose file directory
`docker-compose build `
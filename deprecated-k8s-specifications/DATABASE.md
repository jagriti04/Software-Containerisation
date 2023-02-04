INSTALLATION PERSISTENT POSTGRES DATABASE
1. Create dir: "/var/lib/postgresql/data"
2. Create dir: "/mnt/data"

3. Run: "kubectl apply -f db.yaml"
    - ConfigMap
    - Secret
    - PersistentVolume
    - PersistentVolumeClaim
    - Deployment
    - Service (NotePort, change in prod)


4. Info:
    - user: postgres
    - database: postgres
    - password: cG9zdGdyZXM= --> "echo 'cG9zdGdyZXM=' | base64 --decode"
    - port: 30001

5. Testing: "psql -h localhost -U postgres --password -p 30001 postgres"
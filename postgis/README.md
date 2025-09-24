# Geoserver and PostGIS using OCI Database with PostgreSQL

# Prequisites
- Ran on Oracle Linux 9 in public subnet, same VCN as the PostgreSQL database
- OCI Database with PostgreSQL and PostGIS extensions enabled in private subnet
- Open ports for PostgreSQL and Geoserver (8080)


# Install docker
```
sudo yum install -y yum-utils  
sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# Open ports
```
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

# Pull and Run Docker
```
sudo systemctl start docker
sudo docker pull docker.osgeo.org/geoserver:2.28.x
sudo docker run -it -p8080:8080 docker.osgeo.org/geoserver:2.28.x
```
# Open Geoserver
GeoServer's default username and password: Username: admin. Password: geoserver
```
http://[YOUR PUBLIC IP]2:8080/geoserver/
```

# Geoserver and PostGIS using OCI Database with PostgreSQL



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

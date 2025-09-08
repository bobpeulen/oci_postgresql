# OCI PostgreSQL 

- OCI Data Science notebooka as IDE, in same private subnet as OCI PostgreSQL
    - Using FastMCP 
- OCI GenAI





# OCI PostgreSQL as MCP Server

Following https://github.com/crystaldba/postgres-mcp

```
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo dnf -qy module disable postgresql
sudo dnf install -y postgresql16-server
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
sudo systemctl enable postgresql-16
sudo systemctl start postgresql-16
```


Docker
```
sudo yum install -y yum-utils  
sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl start docker
```

MCP
```
sudo docker pull crystaldba/postgres-mcp
```

Claude Desktop
```
sudo dnf install git -y
git clone https://github.com/aaddrick/claude-desktop-debian.git
cd claude-desktop-debian
```
# Build a .deb package (default)

```
bash build.sh
```

# Build an AppImage
./build.sh --build appimage

# Build with custom options
./build.sh --build deb --clean no  # Keep intermediate files

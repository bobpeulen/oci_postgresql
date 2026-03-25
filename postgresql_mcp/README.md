# OCI PostgreSQL 

- OCI Data Science notebooka as IDE, in same private subnet as OCI PostgreSQL
    - Using FastMCP 
- OCI GenAI



http://130.61.100.26xxx:8000/sse

# OCI PostgreSQL as MCP Server

Following https://github.com/crystaldba/postgres-mcp

```
docker run -p 8000:8000 \
  -e DATABASE_URI=postgresql://bob:xx--167@xx:5432/bpeulen \
  crystaldba/postgres-mcp --access-mode=unrestricted 
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

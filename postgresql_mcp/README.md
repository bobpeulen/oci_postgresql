# Use PostgreSQL MCP Pro with OCI Database with PostgreSQL

The steps use PostgresQL MCP Pro, which can be found [here](https://github.com/crystaldba/postgres-mcp/tree/main).

**Prerequisites:**
- Oracle Linux VM
- Open correct ports (8000) on VM and in security lists
- Create PostgreSQL instance, with ```pg_stat_statements``` enablement.


# Run PostgreSQL MCP Pro - steps

- Install/Start Docker
    ```
    sudo yum install -y yum-utils  
    sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
    sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo systemctl start docker
    ```

- Run the MCP server.
Change the user name, password, endpoint, and database in the below.
    ```
    sudo docker run -p 8000:8000 \
      -e DATABASE_URI=postgresql://[USER_NAME]:[PASSWORD]@[ENDPOINT]:5432/[DATABASE] \
      crystaldba/postgres-mcp --access-mode=unrestricted --transport=sse
    ```



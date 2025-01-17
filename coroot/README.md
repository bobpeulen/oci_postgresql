# Coroot OCI PostgreSQL Monitoring

- Create OCI PostgreSQL instance with pg_stat_statements
- Create jumphost in same VCN, public subnet
- Install postgresql client on jumphost, connect to OCI PostgreSQL
- Open ports/firewalld


## Create extension
```
create extension pg_stat_statements;
select * from pg_stat_statements; 
```

## Install Docker

- https://oracle-base.com/articles/linux/docker-install-docker-on-oracle-linux-ol8

## Run the coroot container
```
docker run --detach --name coroot-pg-agent \
--env DSN="postgresql://admin:@<HOST>:5432/postgres?connect_timeout=1&statement_timeout=30000" \
ghcr.io/coroot/coroot-pg-agent
```

## Check whether Docker is running
```
sudo docker ps
```

# Open on public_ip:8080

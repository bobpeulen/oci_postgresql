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
sudo docker run --name coroot-pg-1 -p 0.0.0.0:8080:80 \
--env DSN="postgresql://admin:pw@10.20.2.52:5432/postgres?connect_timeout=1&statement_timeout=30000" \
ghcr.io/coroot/coroot-pg-agent

--detach 
```

## Check whether Docker is running
```
sudo docker ps
```

# Open on public_ip:8080



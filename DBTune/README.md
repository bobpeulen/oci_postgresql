# Use DBTune on OCI PostgreSQL

# Create user in OCI PostgreSQL
```
GRANT pg_monitor TO dbtune_agent;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

## Run agent in public subnet, same VCN
```
sudo docker run --restart always \
    -e DBT_DBTUNE_SERVER_URL=https://app.dbtune.com \
    -e DBT_DBTUNE_API_KEY=XX \
    -e DBT_DBTUNE_DATABASE_ID=XXX \
    -e DBT_POSTGRESQL_CONNECTION_URL="postgresql://USERNAME:PASSWORD@HOST:5432/postgres?sslmode=require" \
    -e DBT_POSTGRESQL_INCLUDE_QUERIES=true \
    public.ecr.aws/dbtune/dbtune/agent:latest
```

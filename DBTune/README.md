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
# 1) Create new Config and 2) Change Config to db system

## 1. OCI CLI Create / Update Config

```
export compartment_id=ocid1.compartment.oc1..xxx
export db_version=17
export display_name=config_custom_v1
export shape_instance=VM.Standard.E6.Flex

oci psql configuration create --db-version $db_version --display-name $display_name --compartment-id $compartment_id --shape $shape_instance --db-configuration-overrides file://db-configuration-overrides.json

```

## 2. Change Config to db system
```
export db_system_ocid=ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amxx
export custom_config_ocid=ocid1.postgresqldefaultconfiguration.oc1.eu-frankfurt-1.amaaaaaaxx

oci psql db-system update \
  --db-system-id "$db_system_ocid" \
  --db-configuration-params "{\"applyConfig\":\"RESTART\",\"configId\":\"$custom_config_ocid\"}"
```

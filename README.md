# Connect to OCI PostgreSQL

- Create DB in private subnet
- Create instance in public subnet, same VCN
- Add port 5432 to private subnet security list

## See documentation here: https://www.postgresql.org/download/linux/redhat/

## Run in terminal:
```
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo dnf -qy module disable postgresql
sudo dnf install -y postgresql14-server
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
sudo systemctl enable postgresql-14
sudo systemctl start postgresql-14
```

```rm -rf ~/.pgpass```

## Get the certificate and add
```
sudo nano ./dbsystem.pub
```
# copy/paste the certifcate 

## Test the connection
```psql -h [DB Private IP] -U [user name] -d postgres```

example: psql -h 10.0.1.81 -U admin -d postgres

## Run statement
```select version();```

# Connect as user
```psql "sslmode=verify-full sslrootcert=./dbsystem.pub host=<endpoint_fqdn> hostaddr=[DB private IP] dbname=postgres user=<user_name>"```

# Example
psql "sslmode=verify-full sslrootcert=./dbsystem.pub host=e43jihot7lyhlnh6kat3io357iy43a-primary.postgresql.us-ashburn-1.oc1.oraclecloud.com hostaddr=10.0.1.81 dbname=postgres user=admin"

# Run something
```select version();```


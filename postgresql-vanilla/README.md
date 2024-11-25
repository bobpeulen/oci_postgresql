# Install PostgreSQL V14 on VM

TRY ON PRIVATE SUBNET. SAME VCN. 

- Oracle Linux 8
- Public subnet

- Check available version

```
dnf module list postgresql
```

 install the PostgreSQL repo 
 ```
sudo dnf install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```

install PostgreSQL V14
```
sudo dnf update -y
sudo dnf -qy module disable postgresql
sudo dnf install postgresql14 postgresql14-server
````

Initialize and start
```
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
sudo systemctl start postgresql-14
sudo systemctl enable postgresql-14
```

Status
```
sudo systemctl status postgresql-14
```

Create user with password, on 'postgres' user
```
sudo su - postgres
psql -c "alter user postgres with password 'Blabla1991'"
```

Create DB schema/user and check user
```
sudo -u postgres psql
CREATE USER userbp WITH CREATEDB CREATEROLE PASSWORD 'Blabla1991';
\du
```

Create database and table and add data
```
CREATE DATABASE db_1 OWNER userbp;
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);
INSERT INTO cars (brand, model, year) VALUES ('Ford', 'Mustang', 1964);
INSERT INTO cars (brand, model, year) VALUES ('Volvo', 'Mustang', 1988);
INSERT INTO cars (brand, model, year) VALUES ('Mercedes', 'EQB', 1954);
INSERT INTO cars (brand, model, year) VALUES ('Ford', 'Version', 1962);
```

Open port
```
sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload
sudo setenforce 0
```

# Create new VM to perform pg_dump and pg_restore
- Oracle Linux 8
- Same public subnet as vanilla postgresql db

Install client
```
sudo yum install postgresql

```

Run pg_dump on database
```
pg_dump -U postgres -h 130.61.29.241 -s -E 'UTF8' -d db_1 -f db_1_schema_dump.sql
pg_dump -U postgres -h bp-test-remove.sub05031948250.opensourcedata.oraclevcn.com -s -E 'UTF8' -d db_1 -f db_1_schema_dump.sql
bp-test-remove.sub05031948250.opensourcedata.oraclevcn.com
```


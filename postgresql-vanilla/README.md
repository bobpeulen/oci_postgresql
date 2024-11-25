# Install PostgreSQL V14 on VM


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




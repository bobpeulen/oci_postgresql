# Turn OCI Database with PostgreSQL into RESTful API

# Install docker
Follow e.g., these steps for [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)


# Install PostgREST
```
wget https://github.com/PostgREST/postgrest/releases/download/v14.1/postgrest-v14.1-linux-static-x86-64.tar.xz
tar xJf postgrest-v14.1-linux-static-x86-64.tar.xz
```

# Set up table/schema/grant role
[Follow steps here to add data/set up roles](https://docs.postgrest.org/en/v14/tutorials/tut0.html)


# Configure PostgREST
```
sudo nano tutorial.conf
```
Add the below to the new file. Change the private endpoint, Database, etc.

```
db-uri = "postgres://authenticator:mysecretpassword@10.20.2.63:5432/bpeulen"
db-schemas = "api"
db-anon-role = "web_anon"
```

# Open ports
```
sudo firewall-cmd --permanent --add-port=3000/tcp
sudo firewall-cmd --reload 
```


# Start PostgRES
```
./postgrest tutorial.conf
```

# Test REST response


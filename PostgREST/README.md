# Turn OCI Database with PostgreSQL into RESTful API

The below steps use [PostgREST](https://docs.postgrest.org/en/v14/index.html) to build the example and follows the same steps as their page.


# Install docker on your compute
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
db-uri = "postgres://USER:PASSWORD@PRIVATE_ENDPOINT_DB:5432/bpeulen"
db-schemas = "api"
db-anon-role = "web_anon"
```

# Open ports
Make sure to add port/TCP to your security subnets
```
sudo firewall-cmd --permanent --add-port=3000/tcp
sudo firewall-cmd --reload 
```


# Start PostgREST
```
./postgrest tutorial.conf
```

# Test REST response from local machine
```
curl http://[PUBLIC_IP]:3000/todos
```


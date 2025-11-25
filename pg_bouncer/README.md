# Set up of pg_bouncer in front of OCI PostgreSQL

Often, clients would like to add connection pooling to their OCI Database with PostgreSQL.
The following steps are an example to set up connection pooling, using [PgBouncer](https://www.pgbouncer.org/).

The set up is similar to below simplified architecture. Connections are passed through a Network Load Balancer, with the pg_bouncer instances as backend set.
Following, the pg_bouncer - as the connection pooler - connect to multiple PostgreSQL databases or the invidual nodes, to differentiate between read/write and read-only.

![image](images/img_0.png)

# 1. Set up OCI Database with PostgreSQL
Follow [these steps to set up one or more OCI Database with PostgreSQL deployments](https://docs.oracle.com/en-us/iaas/Content/postgresql/getting-started.htm#database)

- After creating the databases, review the max_connections you have in the database. 
- Make sure to open ports (5432) in your public/private subnet

# 2. Set up Network Load Balancer
Follow [these steps to set up a NLB on OCI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm).
For the back end set, you will need to add the OCI Database with PostgreSQL. Add the port (5432) and the private IP of the database.

An example of the backend set.
![image](images/img_2.png)

# 3. Set up multiple instances of pg_bouncer

The below example uses Oracle Linux 9 and assumes your PostgreSQL database is version 14.

- Install pg_bouncer on the compute. 
  ```
  sudo yum update
  sudo yum install pgbouncer postgresql-client-14
  ```

- Configure the user list
  ```
  sudo vim etc/pgbouncer/userlist.txt
  ```

- Add your username and password of your OCI Database with PostgreSQL instances.
  ```
  "Example_user" "example_password"
  ```


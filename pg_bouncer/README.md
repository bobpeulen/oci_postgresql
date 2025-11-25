# Set up of pg_bouncer in front of OCI PostgreSQL

Often, clients would like to add connection pooling to their OCI Database with PostgreSQL.
The following steps are an example to set up connection pooling, using [PgBouncer](https://www.pgbouncer.org/).


# 1. Set up OCI Database with PostgreSQL
Follow [these steps to set up one or more OCI Database with PostgreSQL deployments](https://docs.oracle.com/en-us/iaas/Content/postgresql/getting-started.htm#database)

After creating the databases, review the max_connections you have in the database. 

# 2. Set up Network Load Balancer
Follow [these steps to set up a NLB on OCI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm).
For the back end set, you will need to add the OCI Database with PostgreSQL. Add the port (5432) and the private IP of the database.

An example of the backend set.
![image](images/img_0.png)

# 3. Set up multiple instances of pg_bouncer


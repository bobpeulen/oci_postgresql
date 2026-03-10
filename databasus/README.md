# Example Databasus set up

```
https://github.com/databasus/databasus
```

- Install Docker
- VM, Public subnet, same VCN as OCI PostgreSQL.
- Open port 4005

```
docker run -d \
  --name databasus \
  -p 4005:4005 \
  -v ./databasus-data:/databasus-data \
  --restart unless-stopped \
  databasus/databasus:latest
```

- Create S3 bucket as storage
Use S3-compatible settings. Follow instructions: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm
  <img width="697" height="602" alt="image" src="https://github.com/user-attachments/assets/5534d9d0-abc1-46a0-b584-3a06869ada61" />

# Add OCI PostgreSQL as DB

- Create user, add grants 
```
GRANT pg_read_all_data TO my_user;
GRANT pg_write_all_data TO my_user;
```

<img width="572" height="487" alt="image" src="https://github.com/user-attachments/assets/7ee4c14f-5759-4d15-906d-bd01c46cb5f3" />

<img width="1530" height="765" alt="image" src="https://github.com/user-attachments/assets/0f1cd461-559f-463e-98eb-637cf4671e0e" />



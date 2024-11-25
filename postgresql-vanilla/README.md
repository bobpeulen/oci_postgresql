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

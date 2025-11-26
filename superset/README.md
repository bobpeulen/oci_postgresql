# Superset + OCI PostgreSQL

## Install and run Docker

- Install Docker
  ```
  sudo apt update
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo apt install docker-ce
  ```

- Start Docker
  ```
  sudo systemctl status docker
  sudo systemctl start docker
  ```

## Open Port and Run Superset

  ```
  git clone --depth=1  https://github.com/apache/superset.git
  cd superset
  sudo docker compose up --build



  sudo firewall-cmd --permanent --add-port=8088/tcp
  sudo firewall-cmd --reload
  ```
## Access
- http://localhost:8088
- Username and default pw are admin

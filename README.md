# Astrolabium-API2

## Requirements
Git \
Docker

If you already have those, you can skip the two first steps

## Installation Steps
Install Git
Install Docker

- Pull the project from GitHub Repository
- Run the YAML File

## Install Git 

On Linux
```Shell
sudo apt-get update
sudo apt-get install git
```
## Install Docker
Install Docker
```Shell
sudo apt update
sudo apt install docker.io
```
Launch Docker
```Shell
sudo systemctl start docker
sudo systemctl enable docker
```
Install Docker Compose
```Shell
sudo apt install curl
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Pull the project from GitHub Repository

Upload the project 
```Shell 
git clone https://github.com/Linker175/Astrolabium-API2.git
cd Astrolabium-API2
```

## Run the YAML file

Place yourself in the right folder and...

Edit the YAML file to replace with your domain name, mail adress and the root password for the MariaDB Container. **Remember to delete the root password from the file afterwards!** .

The domain name is used to get the SSL/TLS Certificates throught LetsEncrypt challenges with HTTP and TCP.
The mail adress is only here to get notifications from LetsEncrypt for things such as certificate renewal and issues
```Shell
nano docker-compose.yml
```

Edit then everything you need inside (username/password that you want for the users inside the database, generate the random key...) **Remember to delete the root password for mariadb from the file afterwards!**

```Shell 
nano docker-compose.yml
```

Run the file inside docker
```Shell
sudo docker-compose up -d
```

Run the creation of the users for mariadb
```Shell
sudo bash database_user.sh
```

Go delete mariadb root password from the two files : 
```Shell
nano docker-compose.yml
```
```Shell
nano variables.py
```

## Some usefull docker commands
### Check status of the containers
```
docker ps -a 
//if status up : running, if status down : stopped
```

### Get container logs
```
docker logs {container name} 
```

## Stop/Start/Delete a container
```
sudo docker stop {dockername1} {dockername2} ... 
sudo docker start {dockername1} {dockername2} ... 
sudo docker rm {dockername1} {dockername2} ... 
```

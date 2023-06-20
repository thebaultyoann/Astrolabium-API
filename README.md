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
Initialise Git
```Shell
git config --global user.name "Yoann Thébault"
git config --global user.email thebaultyoann@gmail.com
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
Run the file inside docker
```Shell
docker-compose up -d  
```

## In the case you want to check the state of the dockers
```
docker ps -a 
//if status up : running, if status down : stopped
```
## In the case you want to relauch the docker 
```
//for the API
sudo docker start mycontainer 
//for the MariaDB
sudo docker start mariaDB
```

## In the case you want to check the logs of a docker (its terminal)
```
sudo docker logs {container_name} 
```

# How it works 

If you run it locally
- localhost/docs

Or if you have a external IP and your server is open to the web
- yourip/docs
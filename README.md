# Astrolabium-API2

## Install Git 

Install Git and Pull the project

```Shell
sudo apt-get update
sudo apt-get install git
git clone https://github.com/Linker175/Astrolabium-API.git
cd Astrolabium-API2
```

Install Docker and the CLI app (and their dependencies) 
Source the venv needed.
Then first launch the app
```
bash download_component.sh
source ../CLI-Admin-test/venv/bin/activate
bash first_run.sh
```



##  Some usefull functions

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

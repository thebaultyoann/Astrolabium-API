# Astrolabium-API2

## Requirements
Git \
Docker

## Installation Steps
Install Git
- Pull the project from GitHup Repository   
Install Docker
- Run the YAML File

## Install Git 

On Linux
```Shell
sudo apt-get update
sudo apt-get install git
```
Init Git
```Shell
git config --global user.name "Yoann Thébault"
git config --global user.email thebaultyoann@gmail.com
```

Upload the project 
```Shell 
mkdir Astrolabium
cd Astrolabium
git remote add origin https://github.com/Linker175/Astrolabium-API2.git
git branch -M main
```

## Install Docker
Set up the repository
```Shell
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```
```Shell
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
```Shell
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Install Docker Repository
```Shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Check that its really installed 
```Shell
sudo docker run hello-world
```
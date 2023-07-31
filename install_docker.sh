#!/bin/bash

#Install Docker
sudo apt update
sudo apt install docker.io

#Launch Docker
sudo systemctl start docker
sudo systemctl enable docker

#Install Docker-Compose
sudo apt install curl
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

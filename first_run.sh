#!/bin/bash

sudo docker-compose up -d 
sleep 8 #wait for the mariadb socket to be up before inputing data inside 
sudo bash database_user.sh

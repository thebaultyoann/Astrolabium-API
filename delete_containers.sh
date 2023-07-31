#!/bin/bash

sudo docker stop mariadb traefik fastapi
sudo docker rm mariadb traefik fastapi

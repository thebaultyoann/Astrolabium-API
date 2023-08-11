#!/bin/bash
sudo bash bash/install_docker.sh 

cd ..
sudo git clone https://github.com/Linker175/CLI-Admin-test.git

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt install python3-pip python3-venv
sudo apt-get install -y apt-transport-https

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash

sudo apt-get update

sudo apt-get install libmariadb3
sudo apt-get install libmariadb-dev

cd CLI-Admin-test
bash cli_first_run.sh

#!/bin/bash
sudo bash bash/install_docker.sh 

cd ..
sudo git clone https://github.com/Linker175/CLI-Admin-test.git

cd CLI-Admin-test
bash cli_first_run.sh

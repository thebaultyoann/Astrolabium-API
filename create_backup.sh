#!/bin/bash

echo "Please enter the root database password: "
read -s password
sudo docker exec mariadb mariadb-dump -uroot -p$password --databases espf_users espf_api > backup.sql
file_size=$(-c %s backup.sql)
file_size_mb=$(echo "scale=2; $file_size_bytes / (1024*1024)" | bc)
echo "The backup is stored in backup.sql and mesure $file_size_mb)"

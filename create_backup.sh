#!/bin/bash

echo "Please enter the root database password: "
read -s password
echo "Please enter the name of the backup you want"
read name
sudo docker exec mariadb mariadb-dump -uroot -p$password --databases espf_users espf_api > $name.sql
file_size=$(bash -c %s backup.sql)
file_size_mb=$(echo "scale=2; $file_size_bytes/1024/1024")
echo "The backup is stored in $name.sql and mesure $file_size_mb"

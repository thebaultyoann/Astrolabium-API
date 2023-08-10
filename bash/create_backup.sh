#!/bin/bash

echo "Please enter the root database password: "
read -s password

echo "Please enter the name of the backup you want: "
read name

sudo docker exec mariadb mariadb-dump -uroot -p$password --databases espf_users espf_api > $name.sql

file_size=$(stat -c%s "$name.sql")
file_size_mb=$(echo "scale=2; $file_size/1024/1024" | bc)

echo "The backup is stored in $name.sql and measures $file_size_mb MB."

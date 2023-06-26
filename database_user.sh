#!/bin/bash

#input here the mariadb root password, then delete it from this file
$mariadbrootpassword="lol"

#Get the data from the Python file to access the variables
source config.py

#User
echo "DB_Username_For_API:$DB_Username_For_API"
echo "DB_Password_For_API:$DB_Password_For_API"

#Admin
echo "DB_User_For_Admin: $DB_User_For_Admin"
echo "DB_Password_For_Admin: $DB_Password_For_Admin"

#databases
echo "DB_Name_For_API: $DB_Name_For_API"
echo "DB_Name_For_Users: $DB_Name_For_Users"

#update users inside mariadb

docker exec -i mariadb mariadb -u root -p$mariadbrootpassword <<EOF
CREATE USER '$DB_Username_For_API'@'%' IDENTIFIED BY '$DB_Password_For_API';
GRANT SELECT ON $DB_Name_For_API.* TO '$DB_Username_For_API'@'%';
GRANT SELECT ON $DB_Name_For_Users.* TO '$DB_Username_For_API'@'%';
EOF

docker exec -i mariadb mariadb -u root -p$mariadbrootpassword <<EOF
CREATE USER '$DB_User_For_Admin'@'%' IDENTIFIED BY '$DB_Password_For_Admin';
GRANT SELECT ON $DB_Name_For_API.* TO '$DB_User_For_Admin'@'%';
GRANT SELECT ON $DB_Name_For_Users.* TO '$DB_User_For_Admin'@'%';
EOF


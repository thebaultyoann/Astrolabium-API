#!/bin/bash

#Get the data from the Python file to access the variables
source ~/../files/variable.py

#MariaDBrootpassword
echo "Mariadb_Root_Password:$Mariadb_Root_Password"

#User
echo "DB_Username_For_API:$DB_Username_For_API"
echo "DB_Password_For_API:$DB_Password_For_API"

#Admin
echo "DB_User_For_Admin: $DB_User_For_Admin"
echo "DB_Password_For_Admin: $DB_Password_For_Admin"

#databases
echo "DB_Container_Name: $DB_Container_Name"
echo "DB_Name_For_API: $DB_Name_For_API"
echo "DB_Name_For_Users: $DB_Name_For_Users"

#update users inside mariadb

sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_Username_For_API'@'%' IDENTIFIED BY '$DB_Password_For_API';
GRANT SELECT ON $DB_Name_For_API.* TO '$DB_Username_For_API'@'%';
GRANT SELECT ON $DB_Name_For_Users.* TO '$DB_Username_For_API'@'%';
EOF

sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_User_For_Admin'@'%' IDENTIFIED BY '$DB_Password_For_Admin';
GRANT SELECT ON $DB_Name_For_API.* TO '$DB_User_For_Admin'@'%';
GRANT SELECT ON $DB_Name_For_Users.* TO '$DB_User_For_Admin'@'%';
EOF


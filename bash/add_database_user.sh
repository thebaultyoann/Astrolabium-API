#!/bin/bash

#Get the data from the Python file to access the variables -> only the 1 or 10 first lines not to show errors 
source <(sed -n '1,10p' files/variable.py)
source <(sed -n '1,16p' files/variable.py)
#update users inside mariadb

#For client users
sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_Username_Users'@'%' IDENTIFIED BY '$DB_Password_Users';
GRANT SELECT ON $DB_Name_For_Users_Tables.users TO '$DB_Username_Users'@'%';
EOF

#For client api
sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_Username_API'@'%' IDENTIFIED BY '$DB_Password_API';
GRANT SELECT ON $DB_Name_For_Api_Tables.* TO '$DB_Username_API'@'%';
EOF

#For Admin user
sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_Username_UserAdmin'@'%' IDENTIFIED BY '$DB_Password_UserAdmin';
GRANT SELECT ON $DB_Name_For_Users_Tables.useradmin TO '$DB_Username_UserAdmin'@'%';
EOF

#For Admin api
sudo docker exec -i $DB_Container_Name mariadb -u root -p$Mariadb_Root_Password <<EOF
CREATE USER '$DB_Username_APIAdmin'@'%' IDENTIFIED BY '$DB_Password_APIAdmin';
GRANT INSERT, UPDATE, DELETE ON $DB_Name_For_Api_Tables.* TO '$DB_Username_APIAdmin'@'%';
EOF

#!/bin/bash
echo ''
echo "Please enter the email you want for your certificate renewal"
read mail

echo ''
echo "Please enter the password you want for the root user of mariadb"
read -s rootpassword

echo ''

cd ..
cd Astrolabium-API2 

sed -i '/MYSQL_ROOT_PASSWORD/s/=.*$/=/' docker-compose.yml    
sed -i '/certificatesresolvers.myresolver.acme.email=/s/=.*$/=/' docker-compose.yml  
sed -i "s/certificatesresolvers.myresolver.acme.email=/&${mail}\"/" docker-compose.yml
sed -i "s/MYSQL_ROOT_PASSWORD=/&${rootpassword}/" docker-compose.yml

sudo docker-compose up -d 

sed -i '/MYSQL_ROOT_PASSWORD/s/=.*$/=/' docker-compose.yml  

source ~/.bashrc

echo ''
echo ''
echo 'Here is you 2FA secret, take it and store it on your computer'
secret=$(python3 bash/generate_2FA_secret.py)
echo $secret

echo ''
echo ''

echo "Please enter the name of admin_user you want for the API: "
read adminname

echo ''

echo "Please enter the password of this admin_user you want for the API:"
read -s adminpassword

echo ''

echo "Please enter the name of user you want for the CLI: "
read cliname

echo ''

echo "Please enter the password you want for the CLI:"
read -s clipassword

sleep 3 #wait for the mariadb socket to be up before inputing data inside 

mariadb_ip=$(sudo bash bash/get_mariadb_ip.sh)

diditwork=$(python3 bash/add_api_useradmin.py $rootpassword $mariadb_ip $adminname $adminpassword $secret) #create admin_user inside db espf_admin 
echo $diditwork

sudo bash bash/add_database_user.sh  #create the mariadb users for API

echo "MariaDB users created"

sudo bash bash/add_cli_user.sh $cliname $clipassword $rootpassword #create cli user -> a MariaDB user

echo "CLI user created"

echo "Installation terminated"
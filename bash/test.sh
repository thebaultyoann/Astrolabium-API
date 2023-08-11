mariadb_ip=$(sudo bash bash/get_mariadb_ip.sh)

echo "Please enter the name of user you want for the CLI: "
read cliname

echo ''

echo "Please enter the password you want for the CLI:"
read -s clipassword

sudo bash bash/add_cli_user.sh $cliname $clipassword $mariadb_ip 'lol' #create cli user -> a MariaDB user

echo $mariadb_ip
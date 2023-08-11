$1 #username
$2 #password
$3 #mariadbip
$4 #mariadb root password


source ~/CLI-User-test/venv/bin/activate

password_hash=$(python3 bash/generate_cli_hash.py $2)

sudo docker exec -i mariadb mariadb -u root -p$4 <<EOF
CREATE USER '$1'@'%' IDENTIFIED BY '$password_hash';
GRANT SELECT, INSERT, UPDATE, DELETE ON espf_users.users TO '$1'@'%';
EOF


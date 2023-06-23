#!/bin/bash

password="lol"

# Création d'un utilisateur avec des autorisations en lecture et écriture
create_user_with_read_write() {
    local username=$1
    local password=$2
    local database=$3

    docker exec -i mariadb mysql -uroot -p${password} -e "CREATE USER '${username}'@'%' IDENTIFIED BY '${password}'"
    docker exec -i mariadb mysql -uroot -p${password} -e "GRANT SELECT, INSERT, UPDATE, DELETE ON ${database}.* TO '${username}'@'%'"
}

# Création d'un utilisateur avec des autorisations en lecture seulement
create_user_with_read_only() {
    local username=$1
    local password=$2
    local database=$3

    docker exec -i mariadb mysql -uroot -p${password} -e "CREATE USER '${username}'@'%' IDENTIFIED BY '${password}'"
    docker exec -i mariadb mysql -uroot -p${password} -e "GRANT SELECT ON ${database}.* TO '${username}'@'%'"
}

# Suppression d'un utilisateur
delete_user() {
    local username=$1

    docker exec -i mariadb mysql -uroot -p${password} -e "DROP USER '${username}'@'%'"
}

# Exemples d'utilisation
create_user_with_read_write 'admin' 'password1' 'astrolabium'
create_user_with_read_write 'admin' 'password1' 'users'
create_user_with_read_only 'reader' 'password2' 'astrolabium'
create_user_with_read_only 'reader' 'password2' 'astrolabium'



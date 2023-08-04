#For Client Users
DB_Username_Users="client"
DB_Password_Users="password"

#For Client API
DB_Username_API="api_client"
DB_Password_API="password"

#For Admin User
DB_Username_UserAdmin="admin"
DB_Password_UserAdmin="password"

#For Admin API
DB_Username_APIAdmin="api_admin"
DB_Password_APIAdmin="password"

#COMMUNE
DB_Container_Name="mariadb"
DB_Name_For_Users_Tables="espf_users"
DB_Name_For_Api_Tables="espf_api"
users_table="users"
userAdmin_table="userAdmin"
#MariaDBRootPassword to be deleted after!
Mariadb_Root_Password="lol"

#Generate your own secret key with the following command, and the replace it under :
# $ openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 #1440 1 jours
ACCESS_TOKEN_ADMIN_EXPIRE_MINUTES = 60

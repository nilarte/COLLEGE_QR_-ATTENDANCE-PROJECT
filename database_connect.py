import mysql.connector

cnx = mysql.connector.connect(user='root', password='rajnish',
                              host='127.0.0.1',
                              auth_plugin='mysql_native_password')
cnx.close()

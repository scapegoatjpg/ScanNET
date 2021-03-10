import mysql.connector

#need to install mysql connector with pip install mysql-connector-python
# need to download xampp software for mysql database
#start apache server and mysql database
#puts tables in a dictionary so that we can store them in the database after we know for sure there is a database

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "scannet"
    )

cursor = con.cursor()

#function to access the database

def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `customer` WHERE `username` =%s AND `password`=%s", tup)
        return (cursor.fetchone())
    except:
        return False

def add_user(tup):
   
    cursor.execute("INSERT INTO `customer`(`username`,`password`) VALUES ( %s, %s)",tup)
    con.commit()
    return True

#def check_user(tup):
  # if cursor.execute("SELECT * FROM `customer` WHERE EXISTS `username`=%s AND `password`=%s",tup):

       #return True









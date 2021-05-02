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
            cursor.fetchall()
            return True
        except:
            return False


   
#save data into customer table
def add_user(tup):
   
    cursor.execute("INSERT INTO `customer`(`firstName`,`lastName`,`username`,`password`) VALUES ( %s, %s, %s, MD5(%s))",tup)
    con.commit()
    return True



#save data into networkactivity table
def network_activity(tup):
   cursor.execute("INSERT INTO `networkactivity`(`IPAddress`,`networkNameSSID`,`packetNum`,`timeStamp`,`source`,`destination`) VALUES( %s, %s, %s, %s, %s, %s)", tup)
   con.commit()
   return True

#save data into networkinfo table
def network_info(tup):
    cursor.execute("INSERT INTO `networkinfo`(`networkNameSSID`,`IPAddress`) VALUES(%s, %s)", tup)
    con.commit()
    return True

def device(tup):
    cursor.execute("INSERT INTO `device`(`IPAddress`, `MACAddress`,`customerName`) VALUES(%s, %s, %s)", tup)
    con.commit()
    return True

    
       









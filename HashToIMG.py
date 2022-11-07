import HackatonImageGenerator
import HackathonEncrypt
import mysql.connector

"""mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test1;")
mycursor.execute("USE test1;")
mycursor.execute("CREATE TABLE IF NOT EXISTS hash_image (hash VARCHAR(200), image BLOB;")
mydb.commit()

def Hash_Assignment(user_count):
    imgName = HackatonImageGenerator(user_count)
    hash = HackathonEncrypt.Encrypt(imgName)

    #Add the relation of imgName and haash


def Hash_To_IMAGE(hash):
     pass
mycursor.execute("INSERT INTO hash_image (hash,image) VALUES(hash,LOAD_FILE('C:/Users/agraw/Downloads/test.txt));')")
mydb.commit()    """
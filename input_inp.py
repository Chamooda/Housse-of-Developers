import mysql.connector
#import HashToIMG

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test2;")
mycursor.execute("USE test2;")
mycursor.execute("CREATE TABLE IF NOT EXISTS flappy_bird (user_id VARCHAR(20), password VARCHAR(20), score int(5), hash VARCHAR(1000));")
mydb.commit()

l=[]

def inp():
    boo1=False
    use_id=input("Enter your username : ")
    passw=input("Enter password : ")
    hash="6678"
    mycursor.execute("SELECT user_id FROM flappy_bird;")
    result=mycursor.fetchall();
    for i in result:
        if str(i[0])==use_id: 
            boo1=True
    if boo1==False:       
        sql="INSERT INTO flappy_bird (user_id,password,score,hash) VALUES(%s,%s,%s,%s)"
        val=(use_id,passw,0,hash)
        mycursor.execute(sql,val)
        mydb.commit()
        log = "Login Successful"
    else:
        mycursor.execute("SELECT user_id,password FROM flappy_bird;")
        result2=mycursor.fetchall()
        if result2[0][1]==passw:
            log = "Login Successful"
        else:
            log = "Login Failed"
    credentials=[use_id,log]
    return credentials


def score(name,sco):
    sql="UPDATE flappy_bird SET score=%s WHERE user_id =%s"
    val=(sco,name)
    mycursor.execute(sql,val)
    mydb.commit()



"""def dislayProfile():
    userid = input("Enter Username to view")
    stment = "SELECT hash FROM flappy_bird where user_id = %s"
    val = (userid,)
    mycursor.execute(stment,val)
    mydb.commit()

    hashls = mycursor.fetchall();
    
    for i in hashls:
        HashToIMG(i)"""





    
    
   


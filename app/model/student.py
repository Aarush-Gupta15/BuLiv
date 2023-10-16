import mysql.connector  


def getConnection():
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Janu#2019",database = "BULIV")  
 
    #creating the cursor object  
    cur = myconn.cursor() 




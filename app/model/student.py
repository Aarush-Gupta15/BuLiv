import mysql.connector  


def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  
 
    #creating the cursor object  
    


def getStudents(firstname,lastnamme,selectcourse):
    getConnection()
    
    mysqlquery = "insert into studentS(FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES (%s, %s, %s, %s)"
    mycursor = mydb.cursor()
    values = (id, fname, lastname, selectcourse)  
    mycursor.execute(mysqlquery, values)
    mydb.commit() 
    
    
import mysql.connector  


def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  
 
    #creating the cursor object  
    


def addstudents(mobilenumber,firstname,lastname,selectcourse):
    getConnection()

    mysqlquery = "insert into studentS(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES (%s, %s, %s,%s)"
    mycursor = myconn.cursor()
    values = (mobilenumber, firstname, lastname, selectcourse)  
    mycursor.execute(mysqlquery, values)
    myconn.commit() 
    print("registeed succesfully")

def printstudents():
    getConnection()

    mysqlquery = "SELECT * FROM STUDENTS"
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    allstudent=mycursor.fetchall()
    return allstudent



    

    
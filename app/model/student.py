import mysql.connector  


def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  
 
    #creating the cursor object  
    

#inserting the values
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

    # mysqlquery = "SELECT * FROM STUDENTS"

    mysqlquery = "select s.ID, MOBILE, FIRST_NAME, SECOND_NAME, COURSE_ID,ROOM_ID from students s LEFT JOIN ROOM_ALLOTMENT ra on s.ID=ra.STUDENT_ID"

    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    allstudent=mycursor.fetchall()
    #print(allstudent)
    return allstudent
#printstudents()



    

    
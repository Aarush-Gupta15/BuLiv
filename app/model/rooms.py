import mysql.connector  


def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  
 
    #creating the cursor object  
    

#inserting the values
def allocatetRoom(studentId,roomType,fromDate,toDate):
    getConnection()

    freeRooms = getFreeRooms(roomType)
    roomToAllocate = freeRooms[0]
    roomIdToAllocate = roomToAllocate[0] 
    
    mysqlquery = "insert into ROOM_ALLOTMENT(STUDENT_ID,ROOM_ID,FROM_DATE,TO_DATE) VALUES (%s, %s, %s,%s)"
    mycursor = myconn.cursor()
    values = (studentId, roomIdToAllocate, fromDate, toDate)  
    mycursor.execute(mysqlquery, values)
    myconn.commit() 
    print("alloted succesfully")
    updateRoomAvilbility(roomIdToAllocate)


def updateRoomAvilbility(roomId):
    getConnection()
    mysqlquery = "UPDATE ROOMS SET AVAILABILITY='BOOKED' WHERE ID = %s"
    mycursor = myconn.cursor()
    values = (int(roomId),)
    mycursor.execute(mysqlquery,values)
    myconn.commit() 
    print("updated succesfully")


def getFreeRooms(roomType):
    getConnection()

    mysqlquery = "SELECT * FROM ROOMS WHERE AVAILABILITY='FREE' AND ROOM_TYPE='" + roomType +"'"
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    allFreeRooms=mycursor.fetchall()
    print(allFreeRooms)
    return allFreeRooms


def printstudents():
    getConnection()

    mysqlquery = "SELECT * FROM STUDENTS"
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    allstudent=mycursor.fetchall()
    #print(allstudent)
    return allstudent
#printstudents()

#allocatetRoom(2,"DOUBLE","2022-05-22","2022=05-26")

    

    
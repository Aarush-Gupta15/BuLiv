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
    if(len(freeRooms) !=0):

        roomToAllocate = freeRooms[0]
        roomIdToAllocate = roomToAllocate[0] 
        noOfStudentsIntheRoom = roomToAllocate[3]
        mysqlquery = "insert into ROOM_ALLOTMENT(STUDENT_ID,ROOM_ID,FROM_DATE,TO_DATE) VALUES (%s, %s, %s,%s)"
        mycursor = myconn.cursor()
        values = (studentId, roomIdToAllocate, fromDate, toDate)  
        mycursor.execute(mysqlquery, values)
        myconn.commit() 
        print("alloted succesfully")
        updateRoomAvilbility(roomIdToAllocate,noOfStudentsIntheRoom)
        return True
    else:
        return False

def updateRoomAvilbility(roomId, noOfStudentsIntheRoom):
    noOfStudentsIntheRoom = noOfStudentsIntheRoom + 1
    getConnection()
    mysqlquery = "UPDATE ROOMS SET NO_STUDENTS=%s WHERE ID = %s"
    mycursor = myconn.cursor()
    values = (noOfStudentsIntheRoom,int(roomId),)
    mycursor.execute(mysqlquery,values)
    myconn.commit() 
    print("updated succesfully")


def getFreeRooms(roomType):
    getConnection()

    mysqlquery = "SELECT * FROM ROOMS WHERE CAPACITY > NO_STUDENTS AND CAPACITY=" + roomType
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    allFreeRooms=mycursor.fetchall()
    print(allFreeRooms)
    return allFreeRooms


# def printstudents():
#     getConnection()

#     mysqlquery = "SELECT * FROM STUDENTS"
#     mycursor = myconn.cursor()
#     mycursor.execute(mysqlquery)
#     allstudent=mycursor.fetchall()
#     #print(allstudent)
#     return allstudent
# #printstudents()

def getRoomById(roomId):
    getConnection()

    mysqlquery = "SELECT * FROM ROOMS WHERE ID =" + roomId
    print(mysqlquery)
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    result=mycursor.fetchall()
    print(result)
    return result

def getAllRooms():
    getConnection()

    mysqlquery = "SELECT * FROM ROOMS"
    print(mysqlquery)
    mycursor = myconn.cursor()
    mycursor.execute(mysqlquery)
    result=mycursor.fetchall()
    print(result)
    return result

# allFreeRooms = getFreeRooms("3")
# print(len(allFreeRooms))
getRoomById("1")
    

    
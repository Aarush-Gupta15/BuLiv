import mysql.connector
 
#inserting student data
def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  


def studentrgr():
    getConnection()
    try:
        cur=myconn.cursor()
        cur.execute("")
        print("rgestired succesfully")
    except:
        myconn.rollback()
    myconn.close()







    
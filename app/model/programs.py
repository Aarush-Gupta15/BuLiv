# programs.py>

import mysql.connector  

def getConnection():
    #Create the connection object   
    global myconn 
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin",database = "BULIV")  
 
    #creating the cursor object  
    


def getPrograms():
    getConnection()
    try:  
        cur = myconn.cursor()     
        #Reading the Employee data      
        cur.execute("select NAME from PROGRAM")  
    
        #fetching the rows from the cursor object  
        result = cur.fetchall()  
        
        
        for x in result:  
            print(x[0]);
          
        return result
    except:  
        myconn.rollback()  
  
    myconn.close()


getPrograms()
#!/usr/bin/env python
#!interpreter [optional-arg]
__author__ = "Aarush Gupta"
__version__ = "1.0"
__maintainer__ = "Aarush Gupta"
__email__ = "E23CSEU0008@bennett.edu.in"
__status__ = "Under Review"


from flask import Flask, render_template,request
from model.programs import *
from model.student import *
from model.rooms import *
#from model.student import*
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    userName = request.form['UserName']
    password = request.form['Password']

    if (userName == 'admin' and password == "1212"):
        return showHome()
    else:
        return "Invalid Username/Password"

@app.route('/home', methods=['GET', 'POST'])
def showHome():
     return render_template('home.html')
     
@app.route('/programs', methods=['GET', 'POST'])
def programs():
    results = getprograms()
    return render_template('programs.html',results=results)

@app.route('/showregisterscreen',methods=['GET','POST'])
def showregisterscreen():
    return render_template('registration.html')
      #return 'registered done'

@app.route('/addStudent',methods=['GET','POST'])
def addStudent():
       # pass
        print("HELLO")
        firstname=request.form['fname']
        lastname=request.form['lname']
        selectedcourse=request.form['program']
        mobilenumber=request.form['mobile']
        #results=getStudents(firstname,lastname,selectedcourse)
        print(firstname,lastname,selectedcourse,mobilenumber)
        addstudents(mobilenumber,firstname,lastname,selectedcourse)
        return render_template('registration_result.html',firstname=firstname,mobilenumber=mobilenumber)

@app.route('/viewstudents', methods=['GET','POST'])
def viewstudents():
        
        allstudents=printstudents()
        return render_template('showstudents.html',results=allstudents)


@app.route('/roomDetails', methods=['GET','POST'])
def roomDetails():
        roomId=request.form['roomId']
        results=getRoomById(roomId)
        # allstudents=printstudents()
        return render_template('showRoomDetails.html',results=results)

@app.route('/viewRooms', methods=['GET','POST'])
def viewRooms():
        
        results=getAllRooms()
        # allstudents=printstudents()
        return render_template('showAllRooms.html',results=results)




@app.route('/showAllocateRoom', methods=['GET','POST'])
def showAllocateRoom():
        
        studentId=request.form['studentId']
        firstname=request.form['fname']
        lastname=request.form['lname']

        return render_template('room-allocation.html',studentId=studentId,firstname=firstname,lastname=lastname)

        print("Show allocate room")


@app.route('/allocateRoom',methods=['GET','POST'])
def allocateRoom():
       
        studentId=request.form['studentId']
        roomType=request.form['roomType']
        fromDate=request.form['fromDate']
        toDate=request.form['toDate']
       
        print(studentId,roomType,fromDate,toDate)
        
        if(allocatetRoom(studentId,roomType,fromDate,toDate)):
            return viewstudents()
        else:
             return "<h3>No room available in this category.</h3>"

       
@app.route('/increaseCap',methods=['GET','POST'])
def increaseCap():
       
        roomid=request.form['roomId']
        currentCap=request.form['currentCap']
        increasecapicity(currentCap,roomid)
        #print(roomid,currentCap)
        return viewRooms()

@app.route('/updatestudent',methods=['GET','POST'])
def updatestudent():
        return render_template('option.html')

@app.route('/studentname',methods=['POST'])
def studentname():
         return render_template('updatestudent.html')

@app.route('/studentupdated',methods=['POST'])
def studentupdated():
        
        firstname=request.form['studentfirstName']
        id=request.form['ROLLNUMBER']
        Lastname=request.form['studentLastName']
        updatestudentdata(firstname,Lastname,id)
        return "updated name succesfully"

@app.route('/studetmobilenumber',methods=['GET','POST'])
def studetmobilenumber():
      return render_template('updatestudentmobilenumber.html')

@app.route('/studetmobilenumberupdate',methods=['POST'])
def studetmobilenumberupdate():
        m_number=request.form['Studentmobilenumber']
        id=request.form['ROLLNUMBER']
        updatestudentmobilenumber(m_number,id)
        return "updated mobile number succesfully"
        

if __name__ == "__main__":
    app.run()
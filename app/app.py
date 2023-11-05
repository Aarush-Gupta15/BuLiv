from flask import Flask, render_template,request
from model.programs import *
from model.student import*
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
        #return "Welcome " + userName
        return render_template('welcome.html')
    else:
        return "Invalid Uzername/Password"


@app.route('/programs', methods=['GET', 'POST'])
def programs():
    results = getprograms()
    return render_template('programs.html',results=results)

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('registration.html')
    if request.method=='POST':
       # pass
        print("HELLO")
        firstname=request.form['fname']
        lastname=request.form['lname']
        selectedcourse=request.form['dropbox']
        results=getStudents(firstname,lastname,selectedcourse)
        return 'registered done'

    

    


    
   



if __name__ == "__main__":
    app.run()
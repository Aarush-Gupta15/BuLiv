from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')
    #return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    userName = request.form['UserName']
    password = request.form['Password']

    if (userName == 'admin' and password == "1212"):
        #return "Welcome " + userName
        return render_template('welcome.html')
    else:
        return "Invalid Username/Password"


if __name__ == "__main__":
    app.run()
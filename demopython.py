from flask import Flask,render_template,request
import pyrebase

Config={'apiKey': "AIzaSyCXzd2Jr9_atva527BgA-gcyBOFUzRcKBI",
  'authDomain': "myfirstone-3292d.firebaseapp.com",
  'databaseURL': "https://myfirstone-3292d-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "myfirstone-3292d",
  'storageBucket': "myfirstone-3292d.appspot.com",
  'messagingSenderId': "284687097593",
  'appId': "1:284687097593:web:1dfc802ffd8fe2d7c1cc28",
  'measurementId': "G-0D0RBEJJS8"}

firebase=pyrebase.initialize_app(Config)
#db= firebase.database()
auth=firebase.auth()

app= Flask(__name__)

@app.route("/")
@app.route("/register")

def basic():
    return render_template("register.html")
@app.route('/display',methods=["POST","GET"])

def mydisplay():
    if request.method=="POST":
        e=request.form.get("email")
        p=request.form.get("password")
        response=auth.sign_in_with_email_and_password(e,p)
        print(response)
    return render_template('/display.html',email=e,password=p)

if __name__ ==  '__main__':
    app.run(debug=True)


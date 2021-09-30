from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def mypage():
     return render_template("parents.html")

@app.route('/me')
def me():
     return render_template("me.html")

@app.route('/contact', methods=['GET', 'POST'] )
def contact():
    if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
     

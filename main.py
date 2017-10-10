from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("user_signup_form.html")

@app.route("/hello", methods=["POST"])
def hello():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    is_error = False 

    if username == "" or len(username) < 3 or len(username) > 20:
        username_error = 'Please enter a valid Username'
        is_error = True 

    if password == "" or len(password) < 3 or len(password) > 20:
        password_error = 'Please enter a valid Password'
        is_error = True 

    if verify_password == "" or verify_password != password:
        verify_password_error = 'Please verify your Password'
        is_error = True 

    if is_error:
       return render_template('user_signup_form.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)
       
    return render_template("hello.html", username=username)


app.run()

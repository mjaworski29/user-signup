from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
    <form action = "/signup" method = "post">
        <label for="Username">Username</label>
        <input id="Username" type="text" name = "Username" />
        <input type ="submit" />
        <label for="Password">Password </label>
        <input id="Password" type="text" name="Password" />
        <input type="submit" />
        <label for="Verify Password"> Verify Password </label>
        <input id="Verify Password" type = "text" name = "Verify Password />
        <input type = "submit" />
        <label for="Email"> Email (optional) </label>
        <input id = "Email" type = "text" name = "Email" />
        <input type = "submit" />
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/signup", methods = ["post"])
def signup():
    Username = request.form["Username"]
    return "<h1>Hello," + Username + '</h1>'

app.run()
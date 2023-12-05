import json
from flask import Flask
from flask import jsonify, redirect, render_template, session, request
from models import User
from API import API


app = Flask(__name__)
app.config["SECRET_KEY"] = "STAFFULKIN"
api = API()


@app.route("/users/<id>")
def user(id):
    # Make request
    user = api.getUser(id=id)
    return render_template("index.html", user=user)


@app.route("/addUser", methods=["post", "get"])
def addUser():
    if request.method == "POST":
        user = User.fromForm(request.form)
        print(user)
        api.addUser(user=user, password="123123")

    return render_template("addUser.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

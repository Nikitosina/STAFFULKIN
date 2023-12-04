import json
from flask import Flask
from flask import jsonify, redirect, render_template, session, request
from models import User


app = Flask(__name__)
app.config["SECRET_KEY"] = "STAFFULKIN"


@app.route("/users/<id>")
def user(id):
    # Make request
    user = User(**User.sample)
    return render_template("index.html", user=user)

@app.route("/addUser")
def addUser():
    return render_template("addUser.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

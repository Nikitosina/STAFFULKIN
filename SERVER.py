import json
from flask import Flask
from flask import (
    jsonify,
    redirect,
    render_template,
    render_template_string,
    session,
    request,
)
from models import User, Goal
from API import API, APIError
from constants import ACCESS_TOKEN_KEY


app = Flask(__name__)
app.config["SECRET_KEY"] = "STAFFULKIN"
api = API()


@app.route("/login", methods=["post", "get"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_id = api.authorizeIfNeeded(
            session=session, username=username, password=password
        )
        return redirect(f"/users/{user_id}")

    return render_template("login.html")


@app.route("/users/<id>")  # 1634794874
def user(id):
    try:
        if ACCESS_TOKEN_KEY not in session:
            return redirect("/login")

        token = session[ACCESS_TOKEN_KEY]
        user = api.getUser(id=id, access_token=token)
        return render_template("index.html", user=user)
    except APIError as e:
        return render_template_string(f"<html>{e}</html>")


@app.route("/users/<id>/goals", methods=["post", "get"])
def user_goals(id):
    try:
        if ACCESS_TOKEN_KEY not in session:
            return redirect("/login")

        token = session[ACCESS_TOKEN_KEY]
        if request.method == "POST":
            goal = Goal.fromForm(request.form)
            print(goal)
            api.addGoal(user_id=id, goal=goal, access_token=token)
            return redirect(f"/users/{id}/goals")

        user = api.getUser(id=id, access_token=token)
        return render_template("goals.html", goals=user.goals)
    except APIError as e:
        return render_template_string(f"<html>{e}</html>")


@app.route("/addUser", methods=["post", "get"])
def add_user():
    try:
        if ACCESS_TOKEN_KEY not in session:
            return redirect("/login")

        token = session[ACCESS_TOKEN_KEY]
        if request.method == "POST":
            user = User.fromForm(request.form)
            print(user)
            user_id = api.addUser(user=user, access_token=token)
            return redirect(f"/users/{user_id}")

        return render_template("addUser.html")
    except APIError as e:
        return render_template_string(f"<html>{e}</html>")


@app.route("/companyTree")
def company_tree():
    try:
        if ACCESS_TOKEN_KEY not in session:
            return redirect("/login")

        token = session[ACCESS_TOKEN_KEY]
        tree = api.getCompanyTree(access_token=token)
        return render_template("companyTree.html", tree=tree)
    except APIError as e:
        return render_template_string(f"<html>{e}</html>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

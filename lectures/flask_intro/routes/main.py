from app import app
from flask import render_template


@app.route("/")
def hello_world():
    a = "KEKLOL"
    return render_template("index.html", variable=a)


@app.route("/kek")
def bla_bla():
    return render_template("kek.html")


@app.route("/name/<name>")
def display_name(name):
    return name


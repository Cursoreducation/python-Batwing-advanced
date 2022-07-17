from app import app
from flask import render_template

@app.route("/")
def hello_world2():
    return render_template("index.html")

@app.route("/add/<int:first_number>/<int:second_number>")
def adding_2_numbera(first_number, second_number):
    s = first_number + second_number
    return render_template("Adding.html", variable=s)

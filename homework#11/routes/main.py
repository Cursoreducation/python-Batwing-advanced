from helpers.file import get_users, write_users
from app import app
from flask import render_template, request, redirect

@app.route("/")
def main():
    search_query = request.args.get("search_query")
    if search_query:

        users = get_users()

        searched_users = []
        for user in users:
            if search_query == user["first_name"] or search_query == user["last_name"] or search_query == user[
                "work_area"]:
                searched_users.append(user)
        if len(searched_users) > 0: 
            return render_template("search_item.html", users=searched_users)
        else:
            return render_template("search_item.html", content="Nothing was found for your query")
    else:
        users = get_users()
        return render_template("index.html", users=users)
@app.route("/user-add")
def user_add():
    return render_template("user-add.html")

@app.route("/users", methods=["POST"])
def save_user():
    users = get_users()
    id = 1
    if len(users) > 0:
        id = len(users) + 1
    user = {
        "id": id,
        "email": request.form.get("email"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "work_area": request.form.get("work_area")
    }
    users.append(user)
    write_users(users)
    return redirect("/")

@app.route("/user-edit/<int:id>")
def edit(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            return render_template("user-add.html", user=user)
    return redirect("/")

@app.route("/users/<int:id>", methods=["POST"])
def update(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("work_area")
    write_users(users)
    return redirect("/")

@app.route("/users/delete/<int:id>")
def delete(id):
    users = get_users()
    del users[id -1]
    write_users(users)
    return redirect("/")


# @app.route("/search", methods=["GET"])
# def search():
#     first_name = request.args.get("first_name")
#     last_name = request.args.get("last_name")
#     work_area = request.args.get("work_area")
#
#     users = get_users()
#     search_users = []
#     for user in users:
#         if id == user["id"] or first_name == user["first_name"] or last_name == user["last_name"] or work_area == user["work_area"]:
#             search_users.append(user)
#     if len(search_users) > 0:
#         return render_template("search_item.html", users=search_users)
#     else:
#         return "Not found user"
#

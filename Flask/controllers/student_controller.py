from flask import request,redirect

# def index():


def add():
    newStudent = {
        "id":request.form["id"],
        "name":request.form["name"],
        "course":request.form["course"],
    }
    return redirect("/")



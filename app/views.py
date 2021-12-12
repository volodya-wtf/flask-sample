from os import readlink
from flask import render_template
from flask import session
from flask import request
from flask import redirect

from app import app
from app import extrasense
from app.db import SessionManager
from app.forms import Answer
from app.extrasense import Extrasense

s = SessionManager(session)

extrasenses = []
for name in ["uno", "duo", "tre"]:
    extrasenses.append(Extrasense(name))


@app.route("/", methods=["GET", "POST"])
def index():

    s.create("count", 0)
    s.create("user", [])
    for e in extrasenses:
        s.create(e.name, [])

    context = {
        "session_object": s,
        "title": "Тестовое задание Петров В.А.",
        "extrasenses": extrasenses,
    }

    return render_template("index.html", context=context)


@app.route("/youranswer", methods=["GET", "POST"])
def youranswer():
    if request.method == "POST":
        # Счетчик попыток
        s.increment("count")

        # Получение пользовательского ввода
        s.append("user", int(request.form["answer"]))

        for e in extrasenses:
            s.append(e.name, e.guess())

        return redirect("/")

    form = Answer()

    context = {
        "session_object": s,
        "title": "Тестовое задание Петров В.А.",
        "extrasenses": extrasenses,
    }

    return render_template(
        "youranswer.html", context=context, form=form)
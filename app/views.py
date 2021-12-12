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

    def accuracy(l1, l2: list) -> str:
        acc = 0
        for i, j in zip(l1, l2):
            if i == j:
                acc += 1
        return f"{acc}/{len(l1)}"
    
    s.create("count", 0)
    s.create("user", [])
    for e in extrasenses:
        s.create(e.name, [])

    context = {
        "count": s.fetch("count"),
        "title": "Тестовое задание Петров В.А.",
        "extrasenses": extrasenses,
        "session": session,
    }

    return render_template("index.html", context=context, accuracy=accuracy)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Счетчик попыток
        s.increment("count")

        # Получение пользовательского ввода
        s.append("user", int(request.form["answer"]))

        for e in extrasenses:
            s.append(e.name, e.oracle())

        return redirect("/")

    form = Answer()
    return render_template("form.html", form=form)

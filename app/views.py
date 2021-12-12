from flask import render_template
from flask import session
from flask import request
from flask import redirect

from app import app
from app.db import SessionManager
from app.forms import Answer
from app.extrasense import Extrasense


extrasenses = []
for name in ["uno", "duo", "tre"]:
    extrasenses.append(Extrasense(name))

s = SessionManager(session)



@app.route("/", methods=["GET"])
def index():


    # Инициализация переменных в хранилище:
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

        # Догадки экстрасенсов:
        for e in extrasenses:
            s.append(e.name, s.fetch(e.name+"_guess"))
            s.assign(e.name+"_guess", None)

        return redirect("/")

    form = Answer()

    
    # Догадки экстрасенсов:
    for e in extrasenses:
        if s.fetch(e.name+"_guess") != None:
            continue
        s.assign(e.name+"_guess", e.guess())

    context = {
        "session_object": s,
        "title": "Тестовое задание Петров В.А.",
        "extrasenses": extrasenses,
    }

    return render_template(
        "youranswer.html", context=context, form=form)
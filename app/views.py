from flask import render_template
from flask import session
from flask import request
from flask import redirect
import flask

from flask.views import View, MethodView

from app import app
from app import extrasense
from app.db import SessionManager
from app.forms import Answer
from app.extrasense import Extrasense, extrasense_factory


s = SessionManager(session)

extrasenses = extrasense_factory(names=['uno', 'duo', 'tre'])

class Index(View):
    def __init__(self):
        s.create("count", 0)
        s.create("user", 0)
        for e in extrasenses:
            s.create(e.name, [])
            s.create(e.name+"_score", 0)

    def dispatch_request(self):
        context = {
            "session_object": s,
            "title": "Тестовое задание Петров В.А.",
            "extrasenses": extrasenses,
        }

        return render_template("index.html", context=context)


class YourAnswer(MethodView):
    def get(self):
        # Догадки экстрасенсов:
        for e in extrasenses:
            if s.fetch(e.name + "_guess") != None:
                continue
            s.assign(e.name + "_guess", e.guess())

        context = {
            "session_object": s,
            "title": "Тестовое задание Петров В.А.",
            "extrasenses": extrasenses,
        }

        form = Answer()

        return render_template("youranswer.html", context=context, form=form)

    def post(self):
        # Увеличение счетчика испытаний
        s.increment("count")

        # Получение пользовательского ввода
        s.assign("user", int(request.form["answer"]))
        

        # Добавление догадок экстрасенсов в хранилище
        # Запись последнего результата в экземпляр Extrasense
        for e in extrasenses:
            s.append(e.name, s.fetch(e.name + "_guess"))
            s.assign(e.name+"_score", e.accuracy(s.fetch("user"), s.fetch(e.name+"_guess"), s.fetch(e.name+"_score")))
            s.assign(e.name + "_guess", None)


        return redirect("/")


app.add_url_rule("/youranswer/", view_func=YourAnswer.as_view("youranswer"))
app.add_url_rule("/", view_func=Index.as_view("index"))

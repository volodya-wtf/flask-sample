from os import readlink
from flask import render_template
from flask import session
from flask import request
from flask import redirect

from app import app

import random

from app.forms import Answer

class Extrasense(object):
    def __init__(self, name):
        self.name = name
    
    def oracle(self):
        return random.randrange(10,99)

uno = Extrasense("uno")
duo = Extrasense("duo")
tre = Extrasense("tre")

def accurcy(l1, l2 : list) -> str:
    acc = 0
    for i, j in zip(l1, l2):
        if i == j:
            acc += 1
    return f'{acc}/{len(l1)}'


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'uno' not in session:
        session['uno'] = []
    if 'duo' not in session:
        session['duo'] = []
    if 'tre' not in session:
        session['tre'] = []
    if 'user' not in session:
        session['user'] = []

    def accuracy(l1, l2 : list) -> str:
        acc = 0
        for i, j in zip(l1, l2):
            if i == j:
                acc += 1
        return f'{acc}/{len(l1)}'

    context = {
        'count': session['count'], 
        'title' : 'Тестовое задание Петров В.А.',
        'extrasenses': [uno, duo, tre],
        'session': session
        }

    return render_template('index.html', context=context, accuracy=accuracy)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Получение пользовательского ввода    
        if 'user' in session:
            results = session.get('user')
            results.append(int(request.form['answer']))
            session['user'] = results
        else:
            session['user'] = [int(request.form['answer'])]

        # Cчетчик попыток
        if 'count' in session:
            session['count'] = session.get('count') + 1
        else:
            session['count'] = 1

        # Ответы экстрасенсов
        if 'uno' in session:
            results = session.get('uno')
            results.append(uno.oracle())
            session['uno'] = results
        else:
            session['uno'] = []
    
        if 'duo' in session:
            results = session.get('duo')
            results.append(duo.oracle())
            session['duo'] = results
        else:
            session['duo'] = []
    
        if 'tre' in session:
            results = session.get('tre')
            results.append(tre.oracle())
            session['tre'] = results
        else:
            session['tre'] = []
  
        return redirect('/')

    form = Answer()
    return(render_template('form.html', form=form))

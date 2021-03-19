from enum import Enum

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/load_zadanie_1', methods=('GET', 'POST'))
def load_zadanie_1():
    return render_template('1.html')


@app.route('/zadanie_1', methods=('GET', 'POST'))
def zadanie_1():
    return 'You sent : {}'.format(request.form['1'])


@app.route('/load_zadanie_2', methods=('GET', 'POST'))
def load_zadanie_2():
    return render_template('2.html')


@app.route("/zadanie_2", methods=('GET', 'POST'))
def zadanie_2():
    x = int(request.form['2_1'])
    y = int(request.form['2_2'])
    mode = request.form['mode']
    cases = {
        "sum": lambda a, b: a + b,
        "subtraction": lambda a, b: a - b,
        "multiplication": lambda a, b: a * b,
        "division": lambda a, b: a / b,
        "exponentiation": lambda a, b: pow(a, b),
        "root": lambda a, b: pow(a, 1 / b),
    }

    if mode == "division" and y == 0:
        return "Error: Dividing by 0"
    elif mode == "root" and y == 0:
        return "Error: Root of 0"
    else:
        return 'Result : ' + str(cases[mode](x, y))


@app.route('/load_zadanie_3', methods=('GET', 'POST'))
def load_zadanie_3():
    return render_template('3.html')


@app.route("/zadanie_3", methods=('GET', 'POST'))
def zadanie_3():
    login = "admin"
    password = "admin"
    login_session = request.form['3_1']
    password_session = request.form['3_2']
    if login == login_session and password_session == password:
        return load_zadanie_2()
    else:
        return render_template('3.html', value=login_session) + "<strong>Złe hasło</strong>"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

from flask import Flask, request, session, render_template
import datetime
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mP0XjJwAqQAAAIEA3lsqF1ITx+ayl+q0BymZ2gw43A4VvXQMU8JnPy45"


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/load_zadanie_1', methods=('GET', 'POST'))
def load_zadanie_1():
    return render_template('login.html')


@app.route('/load_account', methods=('GET', 'POST'))
def load_account():
    return render_template('account.html', username_session=session['username'])


@app.route('/account', methods=('GET', 'POST'))
def account():
    age = (datetime.now() - session['timestamp'])
    if age > datetime.timedelta(seconds=5):
        logout()
    if request.form.get("Logout") == 'Logout':
        logout()
    return


@app.route('/login', methods=('GET', 'POST',))
def login():
    username = "admin"
    password = "admin"
    username_session = request.form['username']
    password_session = request.form['password']
    if username == username_session and password_session == password:
        session['username'] = username_session
        session['timestamp'] = datetime.now()
        return load_account()
    else:
        return render_template('login.html', value=username_session) + "<strong>Złe hasło</strong>"


@app.route('/logout', methods=('GET', 'POST',))
def logout():
    del session['username']
    return load_zadanie_1()


if __name__ == '__main__':
    app.run()

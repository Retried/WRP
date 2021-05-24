from framework import Framework

app = Framework()


@app.route('/example')
def example():
    print("Hello World!")


@app.route('/user/([a-zA-Z0-9-_')
def user(who):
    print("user: ", who)


@app.route('/hello')
def hello():
    print("Ala ma kota")


print(app.url_for('example'))

app.run()

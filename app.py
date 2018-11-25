from flask import Flask, redirect, session

from lab_1.routes import lab_1
from lab_2.routes import lab_2
from lab_3.routes import lab_3

app = Flask(__name__)
app.register_blueprint(lab_1, url_prefix='/lab_1')
app.register_blueprint(lab_2, url_prefix='/lab_2')
app.register_blueprint(lab_3, url_prefix='/lab_3')
app.secret_key = 'hello'

# from lab_2.routes import *


@app.route('/')
def hello_world():
    session.clear()
    return redirect('lab_1')


if __name__ == '__main__':
    app.run()

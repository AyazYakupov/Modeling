from flask import Flask, redirect
from lab_3.routes import lab_3

app = Flask(__name__)
app.register_blueprint(lab_3, url_prefix='/lab_3')
app.secret_key = 'hello'

from lab_2.routes import *


@app.route('/')
def hello_world():
    session.clear()
    return redirect('lab_2')


if __name__ == '__main__':
    app.run()

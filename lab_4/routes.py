from flask import Blueprint, render_template, request
from .test2 import *

lab_4 = Blueprint('lab_4', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/lab_4/static')


@lab_4.route('/', methods=['GET', 'POST'])
def lab_4_getter():
    tables = [{'h2': 'Exp(x)'}, {'h2': '(a0 * x) / (a1 + a2 * x)'}]
    if request.method == 'GET':
        return render_template('lab_4.html', tables=tables, current_lab='Lab 4')
    elif request.method == 'POST':
        a0 = int(request.form.get('a0'))
        a1 = int(request.form.get('a1'))
        a2 = int(request.form.get('a2'))
        p = int(request.form.get('p'))
        table_1, table_2 = main(p=p, a0=a0, a1=a1, a2=a2)
        tables[0]['data'] = list(table_1)
        tables[1]['data'] = list(table_2)
        return render_template('lab_4.html', tables=tables, current_lab='Lab 4')

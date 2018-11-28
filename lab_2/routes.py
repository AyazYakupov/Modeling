from app import session
import matplotlib.pyplot as plt
import numpy as np
from flask import request, jsonify, Blueprint, render_template

lab_2 = Blueprint('lab_2', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/lab_2/static')


@lab_2.route('/', methods=['GET', 'POST'])
def myapp():
    degree = session.get('degree')
    size = session.get('size')
    return render_template('new.html', table=session.get('table'), degree=degree, size=size, current_lab='Lab 2')


@lab_2.route('/create_table', methods=['GET', 'POST'])
def create_table():
    size = int(request.form.get('points'))

    x = np.linspace(0, 5, size)
    y = np.zeros(size)
    a = np.random.normal(0, 2, size=size)
    y = x ** 2 + a

    session['size'] = size
    session['table'] = list(zip(np.round(x, 3), np.round(y, 3), [1 for i in range(size)]))
    return jsonify(result='Okey')


@lab_2.route('/polyfit', methods=['GET', 'POST'])
def polyfit():
    polynom_degree = int(request.form.get('degree'))

    x = [i[0] for i in session['table']]
    y = [i[1] for i in session['table']]

    w = [int(i) for i in request.form.get('weight').strip().split()]

    x_array = []

    for i in range(len(x) - 1):
        x_array.extend(np.linspace(x[i], x[i + 1], 10))

    p = np.polyfit(x, y, polynom_degree, w=w)  # вычисление коэффициентов многочлена
    yp = np.polyval(p, x_array)  # вычисление значений многочлена

    plt.plot(x, y, 'ro', label=u'Function')
    plt.plot(x_array, yp, 'r', label='Approx')

    std = np.sqrt((y - yp[::9]) ** 2)
    plt.errorbar(x, y, std, label=u'Std')
    plt.legend(loc='best')
    plt.title(u'Plots')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    plt.savefig('static/lab_2/images/plot.png')
    plt.close()

    session['degree'] = polynom_degree
    session['url'] = 'images/plot.png'

    return jsonify(result=session['url'])


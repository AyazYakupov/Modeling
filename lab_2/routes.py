import matplotlib.pyplot as plt
import numpy as np
from flask import render_template, session, jsonify, request

from app import app


@app.route('/lab_2', methods=['GET', 'POST'])
def myapp():
    degree = session.get('degree')
    size = session.get('size')
    return render_template('new.html', table=session.get('table'), degree=degree, size=size)


@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    size = int(request.form.get('points'))

    x = np.linspace(0, 5, size)
    y = np.zeros(size)
    a = np.random.normal(0, 2, size=size)
    y = x ** 2 + a

    session['size'] = size
    session['table'] = list(zip(np.round(x, 3), np.round(y, 3), [1 for i in range(size)]))
    return jsonify(result='Okey')


@app.route('/polyfit', methods=['GET', 'POST'])
def polyfit():
    polynom_degree = int(request.form.get('degree'))

    x = [i[0] for i in session['table']]
    y = [i[1] for i in session['table']]

    w = [int(i) for i in request.form.get('weight').strip().split()]

    # A = np.vstack([x, np.ones(len(x))]).T

    # аппроксимация многочленом 2 степени по МНК
    p = np.polyfit(x, y, polynom_degree, w=w)  # вычисление коэффициентов многочлена
    yp = np.polyval(p, x)  # вычисление значений многочлена

    plt.plot(x, y, 'ro', label=u'Function')
    plt.plot(x, yp, 'r', label='Approx')
    std = np.sqrt((y - yp) ** 2)
    plt.errorbar(x, y, std, label=u'Std')
    plt.legend(loc='best')
    plt.title(u'Plots')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    plt.savefig('static/lab_3/images/plot.png')
    plt.close()

    session['degree'] = polynom_degree
    session['url'] = 'static/lab_3/images/plot.png'

    return jsonify(result=session['url'])

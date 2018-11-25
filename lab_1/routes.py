from math import sqrt

from flask import request, jsonify, Blueprint, render_template

from .engine import *

lab_1 = Blueprint('lab_1', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/lab_1/static')


@lab_1.route('/', methods=['GET', 'POST'])
def lab_1_getter():
    if request.method == 'GET':
        array = [(i, i ** 3) for i in range(-10, 11, 1)]
        return render_template('lab_1.html', array=array, current_lab='Lab 1')

    elif request.method == 'POST':
        array = [(i, i ** 3) for i in range(-10, 11, 1)]

        x = float(request.form['X'])
        n = int(request.form['N'])

        peace_of_array = get_numbers_from_array(x, n, array)
        y = round(x ** 3, 3)

        result = round(formule_solution(peace_of_array, x), 3)

        return render_template('lab_1.html', array=array, y=y, result=result, x=x, n=n, current_lab='Lab 1')


@lab_1.route('/reverse', methods=['GET', 'POST'])
def reverse_interpolation():
    array = [(i ** 3, i) for i in range(-10, 11, 1)]
    y = 0
    n = int(request.form['N'])
    peace_of_array = get_numbers_from_array(y, n, array)
    result = round(formule_solution(peace_of_array, y), 3)
    f = sqrt(sqrt(y))
    return jsonify(result=result, f=f)

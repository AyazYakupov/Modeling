from flask import Blueprint, render_template, abort
from flask import jsonify, request
from jinja2 import TemplateNotFound

from .test import get_x

lab_3 = Blueprint('lab_3', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/lab_3/static')


@lab_3.route('/', methods=['GET', 'POST'])
def gauss_integration():
    try:
        return render_template('lab3.html', current_lab='Lab 3')
    except TemplateNotFound:
        abort(404)


@lab_3.route('/get_answer', methods=['POST'])
def get_answer():
    func_value = request.form.get('func')
    N = request.form.get('N')
    print(func_value, N)
    print(request.form)
    result = str(get_x(float(func_value), int(N)))
    print(result)
    return jsonify(result=result)

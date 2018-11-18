from math import e, pi, sqrt

from scipy.integrate import fixed_quad


def f(x):
    return e ** -((x ** 2) / 2)


def get_x(func_val, n):
    if func_val >= 0.5:
        return 4.99999
    i = 0.00001
    while True:
        num = (fixed_quad(f, 0, i, n=n)[0] / sqrt(2 * pi))
        if num >= func_val:
            return round(i, 5)
        else:
            i += 0.00001

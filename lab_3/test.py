from math import e, pi, sqrt

from scipy.integrate import fixed_quad


def f(x):
    return e ** -((x ** 2) / 2)


def get_x(func_val, n):
    if func_val >= 0.5:
        return 4.99999
    a = 0
    b = 5
    while True:
        num = (fixed_quad(f, 0, (a + b) / 2, n=n)[0] / sqrt(2 * pi))
        if num < func_val + 0.00000001 and num > func_val - 0.00000001:
            return round((a + b) / 2, 5)
        elif num < func_val:
            a = (a + b) / 2
        elif num > func_val:
            b = (a + b) / 2

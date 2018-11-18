import numpy as np
import sympy as sp
import pandas as pd
from math import e

x_array = np.linspace(0, 9, 10)
np.set_printoptions(formatter={'all': lambda x: str(x)})

x = sp.Symbol('x')
y = e ** x
res = sp.diff(y)


def func_1(x):
    return e ** x


def func_2(x):
    return (10 * x) / (12 + 4 * x)


df = pd.DataFrame({'x': x_array})

df['y'] = func_1(df['x'])
df["y diff 1"] = [None] + [i for i in np.around(np.diff(df['y']), decimals=5)]
df["y diff 2"] = [None, None] + [i for i in np.around(np.diff(df['y'], n=2), decimals=5)]

# y1_array = [func_1(x) for x in x_array]
# y2_array = [func_2(x) for x in x_array]
print(res)

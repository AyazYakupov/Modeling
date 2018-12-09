import numpy as np
import pandas as pd

x_array = np.linspace(1, 10, 10)
np.set_printoptions(formatter={'all': lambda x: str(x)})


def func_1(x):
    return np.exp(x)


def func_2(a0, a1, a2):
    def wrapped(x):
        return (a0 * x) / (a1 + a2 * x)

    return wrapped


def column_3(arr_x, arr_y):
    return [round((arr_y[i + 1] - arr_y[i]) / (arr_x[i + 1] - arr_x[i]), 3) for i in range(len(arr_x) - 1)]


def column_4(arr_x, arr_y):
    return [round((arr_y[i + 1] - arr_y[i - 1]) / (2 * (arr_x[i + 1] - arr_x[i])), 3) for i in range(1, len(arr_x) - 1)]


def column_5(arr_x, arr_y):
    return [round((arr_y[i + 1] - 2 * arr_y[i] + arr_y[i - 1]) / ((arr_x[i + 1] - arr_x[i])**2), 3) for i in
    # return [round((arr_y[i + 1] - 2 * arr_y[i] + arr_y[i - 1]) / (arr_x[i + 1] - arr_x[i]), 3) for i in
            range(1, len(arr_x) - 1)]


def column_6(arr_y):
    return round((4 * arr_y[1] - 3 * arr_y[0] - arr_y[2]) / 2, 3)


def column_7(arr_y):
    return round((-4 * arr_y[8] + 3 * arr_y[9] + arr_y[7]) / 2, 3)


def Runge_formuls(func, y_arr_diff, int_p):  # int_p = input
    xr_arr = np.linspace(1, 10.5, 20)
    yr_arr = [func(i) for i in xr_arr]

    first_formul = [(yr_arr[i + 1] - yr_arr[i]) / 0.5 for i in range(0, len(yr_arr) - 1, 2)]
    second_formul = [round(y_arr_diff[i] + (y_arr_diff[i] - first_formul[i]) / ((0.5 ** int_p) - 1), 3) for i in
                     range(len(y_arr_diff))]
    return second_formul


def var_alignment(arr_x, arr_y_1, arr_y_2):
    xz = [1 / i for i in arr_x]
    y1z = [np.log(i) for i in arr_y_1]
    # y1z = [1 / i for i in arr_y_1]
    y2z = [1 / i for i in arr_y_2]

    # print(y1z)
    y1z_diff = column_3(arr_x, y1z)
    y2z_diff = column_3(xz, y2z)

    y1z_diff_reversed = [round(y1z_diff[i] * arr_y_1[i], 3) for i in range(len(y1z_diff))]
    # y1z_diff_reversed = [round(y1z_diff[i] * y1z[i], 3) for i in range(len(y1z_diff))]
    y2z_diff_reversed = [round(y2z_diff[i] * (arr_y_2[i] ** 2) / (arr_x[i] ** 2), 3) for i in range(len(y2z_diff))]

    return y1z_diff_reversed, y2z_diff_reversed


def get_df(x_array, func, p):
    df = pd.DataFrame({'x': x_array})
    df['y'] = np.round(func(df['x']), 3)
    df["y'"] = [''] + column_3(df['x'].__array__(), df['y'].__array__())
    df["y2'"] = [''] + column_4(df['x'].__array__(), df['y'].__array__()) + ['']
    df["y''"] = [''] + column_5(df['x'].__array__(), df['y'].__array__()) + ['']
    df["y0'"] = [column_6(df['y'].__array__())] + ['' for i in range(9)]
    df["yn'"] = ['' for i in range(9)] + [column_7(df['y'].__array__())]
    # df['Runge formuls'] = Runge_formuls(func, df["y'"].__array__()[1:], p) + ['']
    df['Runge formuls'] = [''] + Runge_formuls(func, df["y'"].__array__()[1:], p)
    return df


def main(p, a0, a1, a2):
    df1 = get_df(x_array, func_1, p)
    df2 = get_df(x_array, func_2(a0, a1, a2), p)
    df1['var alignment'], df2['var alignment'] = [i + [''] for i in var_alignment(x_array, df1['y'].__array__(),
                                                                                  df2['y'].__array__())]
    return df1.__array__(), df2.__array__()


if __name__ == '__main__':
    print(main(2, 3, 5, 4))

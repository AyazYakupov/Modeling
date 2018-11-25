from functools import reduce


def get_numbers_from_array(x: float, n: int, array: list):
    if x < array[(n + 1) // 2][0]:
        return [array[i] for i in range(n + 1)]
    elif x > array[-1 - (n + 1) // 2][0]:
        return [array[i] for i in range(len(array) - 1 - n, len(array))]
    else:
        for i in range((n + 1) // 2, len(array) - (n + 1) // 2):
            if x >= array[i][0] and x < array[i + 1][0]:
                return [array[i + j - n // 2] for j in range(n + 1)]


def newton_division(arr, level_index=0):
    data = level_processing(arr, level_index)
    if len(data) >= 1:
        data.extend(newton_division(data, level_index=level_index + 1))
    return data


def level_processing(arr, lv_ix):
    data = []
    for i in range(len(arr) - 1):
        data.append([arr[i][0],
                     arr[i + 1][bool(lv_ix)],
                     (arr[i + 1][-1] - arr[i][-1]) / (arr[i + 1][bool(lv_ix)] - arr[i][0])])
    return data


def formule_solution(arr, point):
    arr_len = len(arr)
    arr.extend(newton_division(sorted(arr, key=lambda x: x[0])))
    basic = 1
    iter = 1
    res = 0
    for i in step_iterator(arr, arr_len):
        res += i[-1] * basic
        basic = reduce((lambda a, b: a * b), [point - arr[x][0] for x in range(iter)])
        iter += 1
    return res


def step_iterator(data, index):
    i = j = 0
    while True:
        try:
            yield data[j]
        except IndexError:
            return
        j += index - i
        i += 1


arr = [[0, -2], [1, -5], [2, 0], [3, -4]]
formule_solution(arr, 3)

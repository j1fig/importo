def percentile(array, p):
    if len(array) == 1:
        return array[0]
    n = len(array)
    rank = (p / 100) * (n - 1) + 1
    i = int(rank)
    r = rank - i
    ptile = array[i - 1] + r * (array[i] - array[i - 1])
    return int(ptile)  # we floor the percentile. microseconds is precision enough.


def avg(array):
    a = sum(array) / len(array)
    return int(a)  # we floor the average. microseconds is precision enough.

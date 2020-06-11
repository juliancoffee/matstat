from typing import Sequence, List, TypeVar, Optional
import math

N = TypeVar("N", int, float)

DATA = [91, 95, 85, 85, 96, 87, 98,
        92, 90, 89, 98, 97, 117, 88,
        91, 119, 85, 77, 94, 89, 79,
        108, 94, 112, 96, 93, 98,
        112, 97, 88, 107, 95, 99,
        101, 104, 81, 102, 117, 105,
        104, 103, 107, 100, 85, 105,
        112, 93, 92, 106, 108, 84, 113,
        118, 98, 120, 94, 92, 85, 101,
        108, 119, 96, 94, 92, 102, 109,
        113, 99, 98, 115, 105, 86, 87,
        92, 96, 89, 97, 115, 100, 99,
        119, 97, 89, 99, 90, 79, 91,
        103, 109, 108, 88, 91, 98, 99,
        77, 72, 99, 84, 82, 96]

# Напряму


def dispersion(xs: List[N]) -> float:
    length = len(xs)
    avg = average(xs)
    res = sum([(x - avg)**2 for x in xs]) / length
    return res


def average(xs: Sequence[N]) -> float:
    length = len(xs)
    if not length:
        return 0
    else:
        return sum(xs) / length

# Методом умовних iнтервалiв


def distance_sturges(xs: Sequence[N]) -> int:
    """ Return h of selection """
    n = len(xs)
    m = 1 + 1.322 * math.log(n, 10)
    h = (max(xs) - min(xs)) / m
    return int(h)


def intervals(xs: Sequence[N], h: Optional[int] = None) -> List[List[N]]:
    if h is None:
        h = distance_sturges(xs)
    chunks = []
    buff = []
    index = min(xs) + h
    for x in xs:
        if x <= index:
            buff.append(x)
        else:
            index += h
            chunks.append(buff)
            buff = [x]
    return chunks


def median_longest(intervals: Sequence[List[N]]) -> float:
    biggest = max(intervals, key=len)
    return average(biggest)


def u(interval: List[N], C: float) -> float:
    diff = max(interval) - min(interval)
    if int(diff) == 0:
        h = 1
    else:
        h = int(diff)
    res = (average(interval) - C) / h
    return res


def list_u(intervals: Sequence[List[N]]) -> List[float]:
    C = median_longest(intervals)
    return [u(interval, C) for interval in intervals]


def dispersion_U(xs: List[N], h: Optional[int] = None) -> float:
    if h is None:
        h = distance_sturges(xs)
    list_intervals = intervals(xs, h)
    list_of_u = list_u(list_intervals)
    average_u_sqr = average([u**2 for u in list_of_u])
    average_u = average(list_of_u)
    return h**2 * average_u_sqr - average_u ** 2


def average_U(xs: Sequence[N], h: Optional[int] = None) -> float:
    if h is None:
        h = distance_sturges(xs)
    list_intervals = intervals(xs, h)
    C = median_longest(list_intervals)
    average_u = average(list_u(list_intervals))
    return h * average_u + C

# Мода i медiана


def moda(xs: List[N]) -> N:
    return max(xs, key=xs.count)


def median(xs: List[N]) -> float:
    length = len(xs)
    if length == 1:
        return xs[0]
    elif length % 2 != 0:
        center = int((length + 1) / 2) - 1
        return float(xs[center])
    else:
        first_idx = int(length / 2) - 1
        second_idx = int(length / 2 + 1) - 1
        return (xs[first_idx] + xs[second_idx]) / 2


if __name__ == "__main__":
    selection = sorted(DATA)
    print(f"Moda = {moda(selection)}")
    print(f"Median = {median(selection)}")

    print("\n==(напряму)==")
    print(f"x* = {average(selection)}")
    print(f"Dx* = {dispersion(selection)}")

    print("\n==(метод умовних варiант)==")
    print(f"x* = {average_U(selection)} \n"
          "\t(h за Стерджесом)")
    print(f"Dx* = {dispersion_U(selection)} \n"
          "\t(h за Стерджесом)")

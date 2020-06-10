from typing import Sequence, List
import math

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


def dispersion(xs: List[int]) -> float:
    length = len(xs)
    avg = average(xs)
    return sum(map(
        lambda x: x - avg, xs)
    ) / length


def average(xs: Sequence[int]) -> float:
    length = len(xs)
    return sum(xs) / length

# Методом умовних iнтервалiв


def distance(xs: Sequence[int]) -> int:
    """ Return h of selection """
    n = len(xs)
    m = 1 + 1.322 * math.log(n, 10)
    h = (max(xs) - min(xs)) / m
    return int(h)


def intervals(xs: List[int]) -> List[List[int]]:
    h = distance(xs)
    chunks = []
    buff = []
    index = h
    for x in xs:
        if x <= index:
            buff.append(x)
        else:
            index += h
            chunks.append(buff)
            buff = [x]
    return chunks


def C(xs: List[int]) -> int:
    biggest = max(intervals, key=len)
    return median(biggest)


def dispersion_U(xs: List[int]) -> int:
    pass


def u(interval: List[int], h: int) -> float:
    return 1 / h * h


def average_U(xs: Sequence[int]) -> float:
    h = distance(xs)

# Мода i медiана


def moda(xs: List[int]) -> int:
    return max(xs, key=xs.count)


def median(xs: List[int]) -> float:
    length = len(xs)
    if length % 2 != 0:
        center = (length + 1) / 2
        return float(xs[center])
    else:
        first_idx = int(length / 2)
        second_idx = int(length / 2 + 1)
        return (xs[first_idx] + xs[second_idx]) / 2


if __name__ == "__main__":
    selection = sorted(DATA)
    print(f"Mo = {moda(selection)}")
    print(f"Me = {median(selection)}")
    print(f"x* = {average(selection)}")
    print(f"Dx* = {dispersion(selection)}")

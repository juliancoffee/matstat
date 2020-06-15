import math
from typing import TypeVar


def chi_sqr(k: int, z: float) -> float:
    form = (1 - 2 / (9 * k) + z * math.sqrt(2 / (9 * k))) ** 3
    return k * form


N = TypeVar("N", int, float)


def t_measurement(x_avg: float, a_0: N, n: int, s: float) -> float:
    nominator = (x_avg - a_0) * math.sqrt(n)
    return nominator / s

import math


def chi_sqr(k: int, z: float) -> float:
    form = (1 - 2 / (9 * k) + z * math.sqrt(2 / (9 * k))) ** 3
    return k * form

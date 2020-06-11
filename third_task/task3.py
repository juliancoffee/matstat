from typing import Sequence, List, TypeVar

N = TypeVar("N", int, float)

DATA = [
    91, 95, 85, 85, 96, 87, 98, 92,
    90, 89, 98, 97, 117, 88, 91, 119,
    85, 77, 94, 89, 79, 108, 94, 112,
    96, 93, 98, 112, 97, 88, 107, 95,
    99, 101, 104, 81, 102, 105, 104,
    103, 107, 100, 85, 105, 112, 93,
    92, 106, 108, 84, 113, 98, 120,
    94, 92, 85, 101, 108, 96, 94, 92,
    102, 109, 113, 99, 98, 115, 105,
    86, 87, 92, 96, 89, 97, 100, 99,
    97, 89, 99, 90, 79, 91, 103, 109,
    108, 88, 91, 98, 99, 77, 72, 99,
    84, 82, 96
]


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


def convidence_interval_dispersion():


def convidence_interval_expected_value():
    pass

import math as _math
from ._utils import number


__all__: list[str] = ['simple_prob',
                      'combinations',
                      'permutation']


def simple_prob(favourable: int, total: int) -> number:
    return favourable / total


def combinations(total: int, chosen: int) -> number:
    return _math.factorial(total) // (_math.factorial(chosen) * _math.factorial(total - chosen))


def permutation(total: int, chosen: int) -> number:
    return _math.factorial(total) // _math.factorial(total - chosen)

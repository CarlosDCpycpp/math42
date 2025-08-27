import math
from typing import Callable, NoReturn
from math import gcd
from functools import cache, wraps
from .._utils import number


__all__: list[str] = [
    'root', 'set_up_root', 'simplify_fraction', 'rule_of_3',
    'is_even', 'is_odd', 'is_prime',
    'summation', 'product', 'big_union', 'big_intersection'
    ]


@cache
def root(base: number, root_: number = 2) -> number:
    f"""Calculate the root of the base.\n
    Example:\n
    > root(9, 2)\n
    This returns the square root of 9 (3)\n"""
    return base ** (1/root_)


@cache
def set_up_root(root_: number) -> Callable[[number], number]:
    f"""Returns a function that calculates a specific root.\n
    Example:\n
    > square_root = set_up_root(2)\n
    > x = square_root(16)  # 4"""

    def _root_x(n: number) -> number:
        return n**(1/root_)
    return _root_x


@cache
def simplify_fraction(numerator: int, denominator: int) -> tuple:
    """Simplifies a fraction of "numerator"/"denominator".
    Example:
    > simplify_fraction(12, 16)
    This return a tuple that is equal to (3, 4)."""
    gcd_ = gcd(numerator, denominator)
    return numerator // gcd_, denominator // gcd_


@cache
def rule_of_3(a1: number, b1: number, a2: number) -> number:
    """Finds the x in a rule of a rule of 3.
        Example:
        > rule_of_3(4, 2, 100)
        This returns 50.
        Explanation:
             4  - 2
            100 - x
            x = (2 * 100) / 4"""
    return (b1 * a2) / a1


@cache
def is_even(num: int) -> bool:
    """Checks if the variable "num" is even."""
    return True if num % 2 == 0 else False


@cache
def is_odd(num: int) -> bool:
    """Checks if the variable "num" is odd."""
    return not is_even(num)


@cache
def is_div_by(num: int, divisor: int) -> bool:
    """Checks if the variable "num" is divisible by the variable "divisor"."""
    return True if num % divisor == 0 else False


@cache
def is_prime(num: int) -> bool:
    """Checks if the variable "num" is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


@cache
def summation(n: int, i: int = 1) -> int:
    return sum(range(i, int(n) + 1))


# @cache
def product(n: int, i: int = 1) -> int:
    result: int = 1
    for num in range(i, int(n) + 1):
        result *= num
    return result


@cache
def big_union(*sets: set, i: int = 1) -> set:
    if i >= len(sets):
        return set()
    result: set = set()
    for target_set in sets[i:]:
        result |= target_set
    return result


@cache
def big_intersection(*sets: set, i: int = 1) -> set:
    if i >= len(sets):
        return set()
    result: set = sets[i]
    for target_set in sets[(i + 1):]:
        result &= target_set
    return result

import string as _string
import collections.abc as _c

from ._others.fibonacci import Fibonacci
from ._utils import number


__all__: list[str] = ['fibonacci', 'basic', 'prime', 'roots', 'countdown', 'powers', 'alphabet', 'collatz']


def fibonacci() -> _c.Generator[int]:
    yield from Fibonacci.generator()


def basic(start: int = 1) -> _c.Generator[int]:
    i = start
    while True:
        yield i
        i += 1


def prime() -> _c.Generator[int]:
    """Each call generates the next prime number."""
    num = 2
    while True:
        primes = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if primes:
            yield num
        num += 1


def roots(root: int, start: int = 1) -> _c.Generator[number]:
    """Returns the x root of the consecutive integers (starting from the "start" variable, which, by default, is 0)."""
    n = start
    while True:
        yield n**(1/root)
        n += 1


def countdown(start: int) -> _c.Generator[int]:
    """Each call return the last call's return minus 1, the first call returns the start."""
    while start >= 0:
        yield start
        start -= 1


def powers(exponent: int) -> _c.Generator[int]:
    """Generates the x power of consecutive integers."""
    n = 1
    while True:
        yield n**exponent
        n += 1


def alphabet(lower: bool = False) -> _c.Generator[str]:
    """Each call generates the next letter of the alphabet.
    If the "lower" variable is true (by default, is false), instead of uppercase letters
    the generator returns lowercase letters"""
    if lower:
        x = _string.ascii_lowercase
    else:
        x = _string.ascii_uppercase

    for lt in x:
        yield lt


def collatz(num: int) -> _c.Generator[int]:
    """Generates the collatz sequence starting from the "num" variable (including)."""
    while num != 1:
        yield num
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    yield 1

import string as _string
from collections.abc import Generator

from .fibonacci import Fibonacci
from ._utils import number
from ._utils.meta import MetaUninitializable


__all__: list[str] = ['Generators']


class Generators(metaclass=MetaUninitializable):

    @staticmethod
    def fibonacci() -> Generator[int]:
        """Generates Fibonacci numbers starting from 0.

                Each call returns the next element of the Fibonacci sequence.

                Yields:
                    int: The next Fibonacci number in the sequence.

                Example:
                    >>> fib_gen = Generators.fibonacci()
                    >>> next(fib_gen)
                    0
                    >>> next(fib_gen)
                    1
                """
        yield from Fibonacci.generator()

    @staticmethod
    def basic(start: int = 1) -> Generator[int]:
        i = start
        while True:
            yield i
            i += 1

    @staticmethod
    def prime() -> Generator[int]:
        """Each call generates the next prime number."""
        num = 2
        while True:
            primes = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
            if primes:
                yield num
            num += 1

    @staticmethod
    def roots(root: int, start: int = 1) -> Generator[number]:
        """Returns the x root of the consecutive integers (starting from the "start" variable,
        which, by default, is 0)."""
        n = start
        while True:
            yield n**(1/root)
            n += 1

    @staticmethod
    def countdown(start: int) -> Generator[int]:
        """Each call return the last call's return minus 1, the first call returns the start."""
        while start >= 0:
            yield start
            start -= 1

    @staticmethod
    def powers(exponent: int) -> Generator[int]:
        """Generates the x power of consecutive integers."""
        n = 1
        while True:
            yield n**exponent
            n += 1

    @staticmethod
    def alphabet(lower: bool = False) -> Generator[str]:
        """Each call generates the next letter of the alphabet.
        If the "lower" variable is true (by default, is false), instead of uppercase letters
        the generator returns lowercase letters"""
        if lower:
            tg_alphabet = _string.ascii_lowercase
        else:
            tg_alphabet = _string.ascii_uppercase

        for lt in tg_alphabet:
            yield lt

    @staticmethod
    def collatz(num: int) -> Generator[int]:
        """Generates the collatz sequence starting from the "num" variable (including)."""
        while num != 1:
            yield num
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
        yield 1

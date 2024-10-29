from math42._bases.fibonacii_bases import base_fibonacci_generator
from math42._utils.init_control import MetaUninitializable

from collections.abc import (
    Generator
)


__all__: list[str] = ['Fibonacci']


class Fibonacci(metaclass=MetaUninitializable):

    @staticmethod
    def generator() -> Generator[int]:
        """Each call returns the next element of the fibonacci sequence.
        Starting at 0."""
        yield from base_fibonacci_generator()

    @staticmethod
    def sequence(n: int = 10, include_zero: bool = True) -> list:
        fibonacci = []
        x = base_fibonacci_generator()
        for _ in range(n):
            fibonacci.append(next(x))
        if not include_zero:
            fibonacci.remove(0)
            fibonacci.append(next(x))
        return fibonacci

    # @staticmethod
    def __class_getitem__(cls, n: int, include_zero: bool = True) -> int:
        x = cls.sequence(n, include_zero=include_zero)
        return x[-1]

    @classmethod
    def primes(cls, n: int) -> list:
        def _is_prime(num) -> bool:
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        x = cls.sequence(n)
        z = []
        for j in x:
            if _is_prime(j):
                z.append(j)
        return z

    @classmethod
    def __contains__(cls, n: int) -> bool:
        x = cls.generator()
        while True:
            i = next(x)
            if i == n:
                return True
            elif i > n:
                return False

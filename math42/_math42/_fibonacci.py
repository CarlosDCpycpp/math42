from .._utils.meta import MetaUninitializable
from ._funcs import is_prime, is_even, is_odd
from collections.abc import (
    Generator,
    Callable
)


__all__: list[str] = ['Fibonacci']


class Fibonacci(metaclass=MetaUninitializable):
    """A class to generate Fibonacci numbers and filter sequences.

    This class provides methods to generate Fibonacci numbers, filter them based on certain criteria,
    and cache the results to optimize performance.
    """

    __cache = []
    __cache_initializer = None

    @classmethod
    def generator(cls) -> Generator[int]:
        """Generates Fibonacci numbers starting from 0.

        Each call returns the next element of the Fibonacci sequence.

        Yields:
            int: The next Fibonacci number in the sequence.

        Example:
            >>> fib_gen = Fibonacci.generator()
            >>> next(fib_gen)
            0
            >>> next(fib_gen)
            1
        """
        a, b = 0, 1
        while True:
            if not (a in cls.__cache):
                if len(cls.__cache) > 100:
                    cls.__cache.pop(0)
                cls.__cache.append(a)
            yield a
            a, b = b, a + b

    @classmethod
    def _initialize_cls(cls):
        """Initializes the Fibonacci cache with the first two Fibonacci numbers.

        This method is called to pre-fill the cache with initial values to improve performance
        when generating Fibonacci numbers.
        """
        cls.reset_cls_generator()  # start the class generator
        cls.__cache_initializer = Fibonacci.generator()
        next(cls.__cache_initializer)
        next(cls.__cache_initializer)
        del cls.__cache_initializer

    @classmethod
    def reset_cls_generator(cls):
        cls.__generator = cls.generator()

    @classmethod
    def __iter__(cls) -> Generator[int]:
        """Iterates through the Fibonacci sequence.

        Returns:
            Generator[int]: A generator that yields Fibonacci numbers.
        """
        yield from cls.generator()

    @classmethod
    def __next__(cls) -> int:
        """Returns the next Fibonacci number.

        Returns:
            int: The next number in the Fibonacci sequence.
        """
        return next(cls.__generator)

    @classmethod
    def sequence(cls, length: int, include_zero: bool = True) -> list[int]:
        """Generates a list of Fibonacci numbers.

        Args:
            length (int): The number of Fibonacci numbers to generate. Must be greater than 0.
            include_zero (bool): Whether to include 0 in the sequence. Defaults to True.

        Returns:
            list[int]: A list of the first `length` Fibonacci numbers.

        Raises:
            AssertionError: If `length` is not greater than 0.

        Example:
            >>> Fibonacci.sequence(5)
            [0, 1, 1, 2, 3]
            >>> Fibonacci.sequence(5, include_zero=False)
            [1, 1, 2, 3, 5]
        """
        assert length > 0
        fibonacci = []
        x = cls.generator()
        for _ in range(length):
            fibonacci.append(next(x))
        if not include_zero:
            fibonacci.remove(0)
            fibonacci.append(next(x))
        return fibonacci

    def __class_getitem__(cls, n: int, include_zero: bool = True) -> int:
        """Retrieves the nth Fibonacci number.

        Args:
            n (int): The index of the Fibonacci number to retrieve. Must be greater than 0.
            include_zero (bool): Whether to include 0 in the sequence. Defaults to True.

        Returns:
            int: The nth Fibonacci number.

        Example:
            >>> Fibonacci[5]
            5
        """
        return cls.sequence(n, include_zero=include_zero)[-1]

    @classmethod
    def __contains__(cls, n: int) -> bool:
        """Checks if a number is in the Fibonacci sequence.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if `n` is a Fibonacci number, False otherwise.

        Example:
            >>> 5 in Fibonacci
            True
            >>> 4 in Fibonacci
            False
        """
        gen = cls.generator()
        while cls.__cache[-1] < n:
            cls.__cache.append(next(gen))
        return n in cls.__cache

    @classmethod
    def __get_filtered_sequence(cls, filter_func: Callable, length: int) -> list[int]:
        """Generates a filtered sequence of Fibonacci numbers based on a condition.

        Args:
            filter_func (Callable): A function to filter Fibonacci numbers.
            length (int): The number of filtered Fibonacci numbers to generate.

        Returns:
            list[int]: A list of filtered Fibonacci numbers.
        """
        gen = cls.generator()
        result = []
        while len(result) != length:
            element = next(gen)
            if filter_func(element):
                result.append(element)
        return result

    @classmethod
    def primes(cls, length: int) -> list[int]:
        """Generates a list of prime Fibonacci numbers.

        Args:
            length (int): The number of prime Fibonacci numbers to generate.

        Returns:
            list[int]: A list of prime Fibonacci numbers.

        Example:
            >>> Fibonacci.primes(5)
            [2, 3, 5, 13, 89]
        """
        return cls.__get_filtered_sequence(is_prime, length)

    @classmethod
    def evens(cls, length: int) -> list[int]:
        """Generates a list of even Fibonacci numbers.

        Args:
            length (int): The number of even Fibonacci numbers to generate.

        Returns:
            list[int]: A list of even Fibonacci numbers.

        Example:
            >>> Fibonacci.evens(5)
            [0, 2, 8, 34, 144]
        """
        return cls.__get_filtered_sequence(is_even, length)

    @classmethod
    def odds(cls, length: int) -> list[int]:
        """Generates a list of odd Fibonacci numbers.

        Args:
            length (int): The number of odd Fibonacci numbers to generate.

        Returns:
            list[int]: A list of odd Fibonacci numbers.

        Example:
            >>> Fibonacci.odds(5)
            [1, 1, 3, 5, 21]
        """
        return cls.__get_filtered_sequence(is_odd, length)


Fibonacci._initialize_cls()  # NOQA


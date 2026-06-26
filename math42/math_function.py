from collections.abc import Callable
from enum import Enum
from string import ascii_lowercase

from ._utils import number, raise_if

import numpy as np
import matplotlib.pyplot as plt


class MathFunction:
    def __init__(self, func: Callable[[number], number]) -> None:
        self.func = func

    def __call__(self, item) -> number:
        return self.func(item)

    def show(
            self,
            description: str = None,
            line_space: tuple[int, int, int] = (-10, 10, 400),
            color: str = 'blue',
            __show: bool = True
    ):

        start, stop, points = line_space
        if points <= 0:
            raise ValueError("Line space must have a positive number of points.")

        x = np.linspace(start, stop, points)
        y = [self.func(float(value)) for value in x]

        func_name = description if description is not None else getattr(self.func, "__name__", "f")

        plt.plot(x, y, label=f"y = {func_name}(x)", color=color)

        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title(f"Graph of y = {func_name}(x)")
        plt.legend()
        plt.grid(True)

        if __show:
            plt.show()
        return plt

    def save(
            self, file_name: str,
            description: str = None,
            line_space: tuple[int, int, int] = (-10, 10, 400),
            color: str = 'blue'
    ):
        self.show(
            description=description,
            line_space=line_space,
            color=color
        ).savefig(fname=file_name)


class PolynomialFunc(MathFunction):
    def __init__(self, *coefs: number):  # NoQA
        raise_if(
            ValueError("Polynomials of degree greater than 26 are not supported."),
            len(coefs) > 26
        )
        self._coefs: list = [0 for _ in range(26)]
        for i, coef in enumerate(coefs):
            self._coefs[i] = coef

    @property
    def func(self) -> number:
        return lambda x: sum(v * (x**i) for i, v in enumerate(self.coefs.values()))

    @property
    def coefs(self) -> dict[str, number]:
        return {
            ascii_lowercase[i]: self._coefs[i]
            for i in range(len(self._coefs)+1)
        }

    @property
    def degree(self) -> int:
        return len(self.coefs.keys())

    def __getitem__(self, item: str) -> number:
        return self.coefs.get(item, 0)

    def __setitem__(self, key: str, value: number) -> None:
        raise_if(
            ValueError("Invalid key; key must contain only one char."),
            len(key) != 1
        )
        self._coefs[ascii_lowercase.index(key)] = value


class LinearFunc(MathFunction):

    def __init__(self, a: number, b: number) -> None:  # NoQA
        self._a, self._b = a, b

    @property
    def a(self) -> number: return self._a

    @property
    def b(self) -> number: return self._b

    @property
    def func(self) -> Callable[[number], number]:
        return lambda x: self.a * x + self.b


class QuadFunc(MathFunction):

    def __init__(self, a: number, b: number, c: number) -> None:  # NoQA
        self._a = a
        pass

    class Types(Enum):
        ABC = "ax^2+bx+c"
        AHK = "a(x-h)^2+k"

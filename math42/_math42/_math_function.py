from collections.abc import Callable

from .._utils import number

import numpy as np
import matplotlib.pyplot as plt


class MathFunction:
    def __init__(self, func: Callable[[number], number]) -> None:
        self.func = func

    def __getitem__(self, item) -> number:
        return self.func(item)

    def show(
            self,
            description: str = None,
            linespace: tuple[int, int, int] = (-10, 10, 400),
            color: str = 'blue',
            __show: bool = True
    ):

        start, stop, points = linespace
        if points <= 0:
            raise ValueError("Linespace must have a positive number of points.")

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
            linespace: tuple[int, int, int] = (-10, 10, 400),
            color: str = 'blue'
    ):
        self.show(
            description=description,
            linespace=linespace,
            color=color
        ).savefig(fname=file_name)

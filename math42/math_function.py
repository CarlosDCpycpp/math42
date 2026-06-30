from __future__ import annotations
from collections.abc import Callable

from ._utils import number, raise_if, reduct_num

__all__: list[str] = ['MathFunc', 'PolynomialFunc', 'LinearFunc', 'QuadFunc']


class MathFunc:
    def __init__(self, func: Callable[[number], number]) -> None:
        self._func = func

    @property
    def func(self) -> Callable[[number], number]:
        return self._func

    def __call__(self, item) -> number:
        return self.func(item)

    def show(
            self,
            description: str = None,
            line_space: tuple[int, int, int] = (-10, 10, 400),
            color: str = 'blue',
            __show: bool = True
    ):

        import numpy as np
        import matplotlib.pyplot as plt

        start, stop, points = line_space
        raise_if(
            ValueError("Line space must have a positive number of points."),
            points <= 0
        )
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


class PolynomialFunc(MathFunc):
    def __init__(self, degree_coef_dict: dict[number, number]):  # NoQA
        self._degree_coef_dict = {reduct_num(i): reduct_num(degree_coef_dict[i]) for i in sorted(degree_coef_dict.keys())}

    @property
    def degree(self) -> number:
        return list(self._degree_coef_dict.keys())[-1]

    @property
    def _dc_iter(self):
        return {reduct_num(i): reduct_num(self._degree_coef_dict[i]) for i in sorted(self._degree_coef_dict.keys())[::-1]}.items()

    @property
    def func(self) -> Callable[[number], number]:
        return lambda x: sum([c * (x**d) for d, c in self._dc_iter])

    def __str__(self):
        return ' '.join(
            (lambda lst: lst if lst[2] != '+' else [lst[i] for i in range(len(lst)) if i != 2])(
                (f"y ="
                 f"{' '.join(
                    (f" {'+' if c > 0 else ''} "
                     + (f"{c if c != 1 else ''}x"
                     f"{f'^{d}' if d != 1 else ''}" if d != 0 else str(c)))
                    if c != 0 else ''
                    for d, c in self._dc_iter
                    )}")
                .split())
        ) if sum(self._degree_coef_dict.values()) != 0 else "y = 0"

    @property
    def derivative(self) -> PolynomialFunc:
        return PolynomialFunc({d-1: c*d for d, c in self._dc_iter})

    @property
    def antiderivative(self) -> PolynomialFunc:
        return PolynomialFunc({d+1: c/d for d, c in self._dc_iter})

    @staticmethod
    def _degree_var_return(degree: number) -> Callable:
        return lambda _: reduct_num(lambda s: s._degree_coef_dict[degree])  # NoQA

    def __eq__(self, other: MathFunc):
        if not isinstance(other, PolynomialFunc):
            return False
        return self._dc_iter == other._dc_iter

    def __ne__(self, other: MathFunc):
        return not self.__eq__(other)


class LinearFunc(PolynomialFunc):

    def __init__(self, m: number, b: number) -> None:  # NoQA
        self._degree_coef_dict = {0: b, 1: m}

    @property
    @PolynomialFunc._degree_var_return(1)
    def m(self) -> number: pass  # NoQA

    @property
    @PolynomialFunc._degree_var_return(0)
    def b(self) -> number: pass  # NoQA


class QuadFunc(PolynomialFunc):

    def __init__(self, a: number, b: number, c: number) -> None:  # NoQA
        self._degree_coef_dict = {0: c, 1: b, 2: a}

    @property
    @PolynomialFunc._degree_var_return(2)
    def a(self) -> number: pass  # NoQA

    @property
    @PolynomialFunc._degree_var_return(1)
    def b(self) -> number: pass  # NoQA

    @property
    @PolynomialFunc._degree_var_return(0)
    def c(self) -> number: pass  # NoQA

    @classmethod
    def akh_init(cls, a: number, k: number, h: number) -> QuadFunc:
        return QuadFunc(
            a=a,
            b=-2*a*k,
            c=a+(k**2)+h
        )

    @property
    @reduct_num
    def k(self) -> number:
        return -self.b/(2*self.a)

    @property
    @reduct_num
    def h(self) -> number:
        return self.c - self.a * (self.k**2)

    def __format__(self, format_spec: str) -> str:
        match spec := format_spec.strip().lower():
            case 'akh':
                if self.a == 0:
                    return f"y = {self.c}"
                return (f"y = {self.a if self.a != 1 else ''}"
                        f"{f'(x{'+' if self.k < 0 else '-'}{abs(self.k)})' if self.k != 0 else 'x'}^2"
                        f"{f' {'+' if self.h > 0 else '-'}{abs(self.h)}' if self.h != 0 else ''}")

            case 'abc':
                return str(self)

            case '':
                return '(no specifier passed)'

            case _:
                return f'Unknown specifier: [{spec}]'

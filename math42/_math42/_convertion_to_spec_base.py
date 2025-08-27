from __future__ import annotations

from typing import Union
from abc import ABC, abstractmethod

from .._utils import number, raise_if


class NumberBaseSystem(ABC):

    @staticmethod
    def _convertor(n: int, base: int) -> str:

        digits: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if base == 1:
            return '0' * n
        if base < 0:
            raise ValueError(f'Invalid argument n: "{n}"; n must be >=0.')

        result: str = ''
        while n > 0:
            result = digits[n % base] + result
            n //= base
        return result or '0'

    @classmethod
    @property
    def base_types(cls) -> Union:  # NoQA
        return int | NumberBaseSystem

    def __init__(
            self,
            n: number | str, base: base_types = None
    ) -> None:

        self.__value: int

        if base is None:
            self.__value = int(n)

        elif isinstance(base, int):
            self.__value = int(n, base)

        elif issubclass(base, NumberBaseSystem):
            self.__value = int(n, base.base)  # NoQA

        else:
            raise ValueError(f'Invalid base type: "{base.__class__.__name__}"; base must be either int, NumberBaseSystem or None.')

    @classmethod
    def _quick_init(cls, n, base) -> type:
        QuickBase: type = cls.build('QuickBase', base)  # NoQA
        return QuickBase(n)

    @classmethod
    @property
    @abstractmethod
    def base(cls) -> int:  # NoQA
        pass

    @property
    def value(self) -> int:
        return self.__value

    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)

    def __str__(self) -> str:
        return NumberBaseSystem._convertor(self.value, self.base)

    def __repr__(self) -> str:
        return f'({self!s})[base {self.base}]'

    def __bool__(self) -> bool:
        return bool(self.value)

    def convert(self, base: base_types) -> str:
        if isinstance(base, type) and issubclass(base, NumberBaseSystem):
            return str(base(self.value))
        else:
            return str(self._quick_init(self.value, base))

    def __eq__(self, other: NumberBaseSystem) -> bool:
        return self.value == other.value

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __gt__(self, other: NumberBaseSystem):
        return self.value > other.value

    def __lt__(self, other: NumberBaseSystem):
        return self.value < other.value

    def __ge__(self, other: NumberBaseSystem):
        return self.value >= other.value

    def __le__(self, other: NumberBaseSystem):
        return self.value <= other.value

    @classmethod
    def build(cls, name: str, base: int) -> type:

        raise_if(
            AttributeError(f'The method "{cls.__name__}.build" is not usable; build is only accessible through NumberBaseSystem.',),
            cls.__name__ != NumberBaseSystem.__name__
        )

        return type(
            name,
            (cls,),
            {'base': classmethod(lambda _: base)}
        )


Binary: type = NumberBaseSystem.build('Binary', 2)
Octal: type = NumberBaseSystem.build('Octal', 8)
Duodecimal: type = NumberBaseSystem.build('Duodecimal', 12)
Hexadecimal: type = NumberBaseSystem.build('Hexadecimal', 16)
Sexagesimal: type = NumberBaseSystem.build('Sexagesimal', 60)

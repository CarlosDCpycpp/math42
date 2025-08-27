from .._math42._convertion_bases import units
from .._utils import number
from .._utils.meta import MetaUninitializable
from typing import Callable
from functools import wraps


__all__: list[str] = ['Convert']


# UPDATE THE DOCS
class Convert(metaclass=MetaUninitializable):

    @staticmethod
    def __convertor(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            from_, to, num = func(*args, **kwargs)
            unit_type = func.__name__

            if from_ not in units[unit_type] or to not in units[unit_type][from_]:
                raise TypeError(f"Either '{from_}' or '{to}' is not a recognized unit for {unit_type}.")

            return num * units[unit_type][from_][to]
        return wrapper

    @staticmethod
    @__convertor
    def distance(from_: str, to: str, num: number) -> number:
        """Converts distance between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: mm, cm, dm, m, dam, hm, km.

        Example:
            >>> Convert.distance("m", "km", 1500)
            1.5
        """
        return from_, to, num

    @staticmethod
    @__convertor
    def weight(from_: str, to: str, num: number) -> number:
        """Converts weight between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: mg, g, kg, t.

        Example:
            >>> Convert.weight("kg", "g", 2)
            2000
        """
        return from_, to, num

    @staticmethod
    @__convertor
    def area(from_: str, to: str, num: number) -> number:
        """Converts area between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: mm², cm², dm², m², dam², hm², ha, ac, km².

        Example:
            >>> Convert.area("m2", "ha", 10000)
            1.0
        """
        return from_, to, num

    @staticmethod
    @__convertor
    def volume(from_: str, to: str, num: number) -> number:
        """Converts volume between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: mm³, cm³, dm³, m³, dam³, hm³, km³.

        Example:
            >>> Convert.volume("l", "m3", 1)
            0.001
        """
        return from_, to, num

    @staticmethod
    @__convertor
    def speed(from_: str, to: str, num: number) -> number:
        """Converts speed between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: mm/s, cm/s, dm/s, m/s, dam/s, hm/s, km/h.

        Example:
            >>> Convert.speed("m/s", "km/h", 10)
            36.0
        """
        return from_, to, num

    @staticmethod
    @__convertor
    def time(from_: str, to: str, num: number) -> number:
        """Converts time between units (metric).

        The units must be specified in the `from_` and `to` parameters, where:
        - `from_` is the original unit.
        - `to` is the target unit.

        Accepted units: ms, s, min, h, d, wk, mo, yr.

        Example:
            >>> Convert.time("s", "min", 120)
            2.0
        """
        return from_, to, num


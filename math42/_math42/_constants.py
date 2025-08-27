from typing import (
    final,
    Final
)
from .._utils.meta import MetaUninitializable
from .._utils import number

@final
class Const(metaclass=MetaUninitializable):

    # mathematical
    PI: Final[float] = 3.141592653589793
    EULER_NUMBER: Final[float] = 2.718281828459045  # aka e
    PHI: Final[float] = (1 + (5**0.5))/2  # aka φ (golden ratio)
    IMAGINARY_UNIT: Final[float] = (-1)**0.5  # aka i

    _mathematical: list = [PI, EULER_NUMBER, PHI]
    _mathematical_names: list = ['pi', 'euler number', 'phi', 'imaginary unit']
    __pi, __e, __phi, __i = (
        _mathematical_names[0], _mathematical_names[1],
        _mathematical_names[2], _mathematical_names[3])

    mathematical: dict = {
        __pi: PI,
        __e: EULER_NUMBER,
        __phi: PHI,
        __i: IMAGINARY_UNIT
    }

    # physical
    GRAVITY_ON_EARTH: Final[float] = 9.81  # [m/s] gravitational acceleration on earth
    SPEED_SOUND: Final[float] = 343.0  # [m/s] at 20ºCelsius
    SPEED_LIGHT: Final[float] = 299792458  # [m/s] in vacuum
    GRAVITATIONAL: Final[float] = 6.674e-11  # [m^3/kg/]

    _physical: list = [GRAVITY_ON_EARTH, SPEED_SOUND, SPEED_LIGHT, GRAVITATIONAL]
    _physical_names: list = ['gravity on earth', 'speed sound', 'speed light', 'gravitational']
    (__goe, __ss, __sl, __g) = (
        _physical_names[0], _physical_names[1],
        _physical_names[2], _physical_names[3])

    physical: dict = {
        __goe: GRAVITY_ON_EARTH,
        __ss: SPEED_SOUND,
        __sl: SPEED_LIGHT,
        __g: GRAVITATIONAL
    }

    consts: list = [*_mathematical, *_physical]
    consts_names: list = [*_mathematical_names, *_physical_names]

    consts_table: dict[str, float] = {**mathematical, **physical}

    __name_convertion_table: dict[tuple[str, ...], str] = {
        # [pi] no alias
        ('e', 'euler', 'euler num', 'euler n'): __e,
        ('gr', 'golden ratio'): __phi,
        ('i', 'imaginary'): __i,

        ('goe', 'ge', 'g earth', 'gravity earth'): __goe,
        ('ss', 'sound'): __ss,
        ('sl', 'light', 'c'): __sl,
        ('g', 'gravitational constant', 'gravitational const'): __g
    }

    @staticmethod
    def __convert_name(name: str) -> str:
        filtered_name = name.lower().strip().replace(' ', '_')
        for names, new_name in Const.__name_convertion_table.items():
            if filtered_name in names:
                return new_name
        return name

    def __class_getitem__(cls, name: str) -> str | None:
        key = Const.__convert_name(name)
        return Const.consts_table.get(key, None)

    @classmethod
    def contains(cls, item: number | str) -> bool:
        return item in cls.consts or item.lower().strip() in cls.consts_names
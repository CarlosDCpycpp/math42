from typing import Final
from math import pi
from .._utils.meta import MetaUninitializable
from .._math42.angle_unit_bases import AngleUnitBase


class AngleUnits(metaclass=MetaUninitializable):
    ANGLE: Final[AngleUnitBase] = AngleUnitBase(360)
    RADIANT: Final[AngleUnitBase] = AngleUnitBase(2*pi)

from __future__ import annotations
from .._utils import number


class AngleUnitBase:
    def __init__(self, full_rotation: number):
        self._full_rotation = full_rotation

    @property
    def full_rotation(self) -> number:
        return self._full_rotation

    @property
    def straight(self) -> number:
        return self.full_rotation/2

    @property
    def right(self) -> number:
        return self.full_rotation/4

    @property
    def zero(self) -> int:
        return 0

    def convert(self, n: number, new_unit: AngleUnitBase) -> number:
        return n * new_unit.full_rotation * self.full_rotation**-1

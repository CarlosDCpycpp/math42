from .._utils.meta import MetaUninitializable
from .._utils import number
from ..constants import Const


class Area(metaclass=MetaUninitializable):

    @staticmethod
    def square(side: number) -> number:
        return side**2

    @staticmethod
    def rectangle(side1: number, side2: number) -> number:
        return side1*side2

    @staticmethod
    def parallelogram(base: number, height: number) -> number:
        return base*height

    @staticmethod
    def rhombus(diagonal1: number, diagonal2: number) -> number:
        return (diagonal1*diagonal2)/2

    @staticmethod
    def trapezoid(base1: number, base2: number, height: number) -> number:
        return ((base1+base2)*height)/2

    @staticmethod
    def triangle(base: number, height: number) -> number:
        return 0.5 * base * height

    @staticmethod
    def reg_polygon(n_sides: number, side_length: number, apothem: number) -> number:
        return (0.5 * (n_sides * side_length)) * apothem

    @staticmethod
    def circle(radius: number) -> number:
        return Const.PI * radius**2


class Volume(metaclass=MetaUninitializable):

    @staticmethod
    def cube(side: number) -> number:
        return side**3

    @staticmethod
    def rect_prism(length: number, width: number, height: number) -> number:
        return length * width * height

    @staticmethod
    def pyramid(base_area: number, height: number) -> number:
        return (1/3) * base_area * height

    @staticmethod
    def sphere(radius: number) -> number:
        return (4/3) * Const.PI * radius**3

    @staticmethod
    def cylinder(radius: number, height: number) -> number:
        return Const.PI * radius**2 * height

    @staticmethod
    def cone(radius: number, height: number) -> number:
        return (1/3) * Const.PI * radius**2 * height


class SurfaceArea(metaclass=MetaUninitializable):

    @staticmethod
    def sphere(radius: number) -> number:
        return 4 * Const.PI * radius**2

    @staticmethod
    def cylinder(radius: number, height: number) -> number:
        return 2 * Const.PI * radius * (radius + height)

    @staticmethod
    def cube(edge: number) -> number:
        return Area.square(edge) * 6

    @staticmethod
    def reg_tetrahedron(edge: number) -> number:
        return ((edge**2)*(3**0.5) / 4) * 4


class Pythagoras(metaclass=MetaUninitializable):

    @staticmethod
    def hypotenuse(cathetus_1: number, cathetus_2: number) -> number:
        """Calculates the hypotenuse of a right triangle, takes the catheti as arguments."""
        return (cathetus_1**2 + cathetus_2**2) ** 0.5

    @staticmethod
    def cathetus(hypotenuse: number, other_cathetus: number) -> number:
        """Calculates a cathetus of a right triangle, takes the hypotenuse and the cathetus as arguments."""
        return (hypotenuse**2 - other_cathetus**2) ** 0.5

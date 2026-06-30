from __future__ import annotations
from .angle_units import AngleUnits
from .._math42.angle_unit_bases import AngleUnitBase
from .._utils import number, raise_if, reduct_num, from_private_attr, exclusive_to
from ..math_function import LinearFunc
from ..infinity import Infinity
from typing import Final
from math import pi, acos


__all__: list[str] = [
    'Point2D', 'Vector2D',
    'Line2D', 'LineSegment2D', 'Ray2D',
    'Circle', 'Circumference', 'Arc'
                      ]
# TODO: add regular polygons


class Point2D:

    def __init__(self, x: number = 0, y: number = 0) -> None:
        self._x = x
        self._y = y

    @property
    @from_private_attr
    def x(self) -> number: pass  # NoQA

    @property
    @from_private_attr
    def y(self) -> number: pass  # NoQA

    ORIGIN: Final[Point2D]  # NoQA

    @staticmethod
    def _setup_origin():
        Point2D.ORIGIN = Point2D()  # NoQA

    @property
    def distance_from_origin(self) -> number:
        return LineSegment2D(self, Point2D.origin)  # NoQA

    def __str__(self):
        return f"({self.x};{self.y})"

    def __neg__(self) -> Point2D:
        return Point2D(-self.x, -self.y)
    
    def __sub__(self, other: Point2D | Vector2D) -> Vector2D | Point2D:
        if isinstance(other, Point2D):
            return Vector2D(other, self)
        elif isinstance(other, Vector2D):
            return self + (-other)

    def __isub__(self, other: Vector2D):
        return self - other

    def __add__(self, other: Point2D | Vector2D) -> Vector2D | Point2D:
        if isinstance(other, Point2D):
            return Vector2D(-other, self)
        elif isinstance(other, Vector2D):
            return Point2D(self.x+other.x, self.y+other.y)

    def __iadd__(self, other: Vector2D):
        return self + other

    def __eq__(self, other: Point2D):
        return self.x == other.x and self.y == other.y


class Line2D:
    def __init__(self, slope: number, y_intercept: number):
        self._slope = slope
        self._y_intercept = y_intercept

    @property
    @from_private_attr
    def slope(self) -> number: pass  # NoQA

    @property
    @from_private_attr
    def y_intercept(self) -> number: pass  # NoQA

    def __str__(self):
        return f"y = {self.slope}x + {self.y_intercept}"

    @property
    def func(self) -> LinearFunc:
        return LinearFunc(self.func, self.y_intercept)

    @property
    def directional_vector(self) -> Vector2D:
        return Vector2D(1, self.slope)

    def __contains__(self, item: Point2D) -> bool:
        return self.func(item.x) == item.y

    def __format__(self, format_spec: str):
        match spec := format_spec.lower().strip():
            case "vectorial" | "vector" | "vect" | "v":
                return f"(x,y) = (0,{self.y_intercept}) + t{self.directional_vector!s}"

            case "parametric" | "param" | 'p':
                return f"x = {self.directional_vector.x}t ∧ y = {self.y_intercept} + {self.directional_vector.y}t"

            case '':
                return '(no specifier passed)'

            case _:
                return f'Unknown specifier: [{spec}]'

    def __add__(self, other: Vector2D) -> Line2D:
        return Line2D(self.slope, self.y_intercept+(other.y-other.x))

    def __sub__(self, other: Vector2D) -> Line2D:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> Line2D:
        return self + other

    def __isub__(self, other: Vector2D) -> Line2D:
        return self - other

    def __eq__(self, other: Line2D):
        return self.slope == other.slope and self.y_intercept == other.y_intercept

    def __ne__(self, other: Line2D):
        return not self.__eq__(other)


class Ray2D(Line2D):
    def __init__(  # NoQA
            self,
            slope: number,
            p: Point2D,
            direction: bool = True,
            including: bool = True
    ):
        self._slope: number = slope
        self._edge: Point2D = p
        self._including: bool = including

        # True -> to +inf
        # False -> to -inf
        self._direction: bool = direction

    @property
    @from_private_attr
    def slope(self) -> number: pass  # NoQA

    @property
    @from_private_attr
    def edge(self) -> Point2D: pass  # NoQA

    @property
    @from_private_attr
    def including(self) -> bool: pass  # NoQA

    @property
    @from_private_attr
    def direction(self) -> bool: pass  # NoQA

    @property
    def line(self) -> Line2D:
        return Line2D(self.slope, self.y_intercept)

    @property
    def y_intercept(self) -> number:
        return self.edge.y - self.slope*self.edge.x

    def __str__(self):
        return (f'{self.line!s}, x ∈ '
                f'{f']{Infinity.negative:sp}' if not self.direction 
                    else f'{'[' if self.including else ']'}{self.edge.x}'}'
                f',{f'{Infinity.positive:sp}[' if self.direction
                    else f'{self.edge.x}{']' if self.including else '['}'}')

    def __contains__(self, item: Point2D):
        return (self.func(item.x) == item.y) and\
            (item.x.__ge__ if self.direction else item.x.__le__)(self.edge.x)

    def __add__(self, other: Vector2D) -> Ray2D:
        return Ray2D(self.slope, self.edge+other, self.direction, self.including)

    def __sub__(self, other: Vector2D) -> Ray2D:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> Ray2D:
        return self + other

    def __isub__(self, other: Vector2D) -> Ray2D:
        return self + other

    def __eq__(self, other: Ray2D):
        return self.line == other.line \
            and self.edge == other.edge \
            and self.including == other.including \
            and self.direction == other.direction

    def __ne__(self, other: Ray2D):
        return not self.__eq__(other)


class LineSegment2D:
    def __init__(self, p1: Point2D, p2: Point2D) -> None:
        self.p1 = p1
        self.p2 = p2

    @property
    def length(self) -> number:
        # pythagoras
        return ((self.p1.x+self.p2.x)**2 + (self.p1.y+self.p2.y)**2)**0.5

    @property
    def slope(self) -> number:
        return (self.p1.y-self.p2.y)/(self.p1.x-self.p2.x)

    @property
    def y_intercept(self) -> number:
        return self.p1.y - self.slope*self.p1.x

    @property
    def line(self) -> Line2D:
        return Line2D(self.slope, self.y_intercept)

    def __str__(self):
        return f"{self.line!s}, x∈[{self.p1.x}, {self.p2.x}]"

    def __eq__(self, other: LineSegment2D):
        return self.p1 == other.p1 and self.p2 == other.p2

    def __ne__(self, other: LineSegment2D):
        return not self.__eq__(other)

    def __add__(self, other: Vector2D) -> LineSegment2D:
        return LineSegment2D(self.p1+other, self.p2+other)

    def __sub__(self, other: Vector2D) -> LineSegment2D:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> LineSegment2D:
        return self + other

    def __isub__(self, other: Vector2D) -> LineSegment2D:
        return self - other


class Vector2D:
    def __init__(self, v1: number | Point2D, v2: number | Point2D) -> None:  # NoQA
        raise_if(
            ValueError("For Vector initialization arguments v1 and v2 must share type."),
            type(v1) is not type(v2)
        )
        tp = type(v1)

        if tp == number:
            self._x = v1
            self._y = v2
        elif tp == Point2D:
            self._x = v2.x-v1.x
            self._y = v2.y-v1.y

    @property
    @from_private_attr
    def x(self) -> number: pass  # NoQA

    @property
    @from_private_attr
    def y(self) -> number: pass  # NoQA

    @property
    def point(self) -> Point2D:
        return Point2D(self.x, self.y)

    def __str__(self):
        return f'V{self.point!s}'

    @property
    def norm(self) -> number:
        return LineSegment2D(Point2D.ORIGIN, self.point).length

    def __neg__(self) -> Vector2D:
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other: Vector2D):
        return self.point == other.point

    def __ne__(self, other: Vector2D):
        return not self == other

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> Vector2D:
        return self + other

    def __isub__(self, other: Vector2D) -> Vector2D:
        return self - other


@lambda _: _()
def _setup() -> None:
    Point2D._setup_origin()  # NoQA


class Circumference:
    def __init__(self, center: Point2D, radius: number):
        self._center = center
        self._radius = radius

    @property
    @from_private_attr
    def center(self) -> Point2D: pass  # NoQA

    @property
    @reduct_num
    @from_private_attr
    def radius(self) -> number: pass  # NoQA

    @property
    @reduct_num
    def perimeter(self) -> number:
        return 2*pi*self.radius

    def __contains__(self, item: Point2D) -> bool:
        return LineSegment2D(self.center, item).length == self.radius

    def __str__(self):
        return f"{self.__class__.__name__}(center={self.center!s}; radius={self.radius})"

    @property
    @exclusive_to('Circumference')
    def circle(self) -> Circle:
        return Circle(self.center, self.radius)

    def __eq__(self, other: Circumference):
        if type(self) is not type(other):
            return False
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other: Circumference):
        return not self.__eq__(other)

    def __add__(self, other: Vector2D) -> Circumference:
        return type(self)(self.center+other, self.radius)

    def __sub__(self, other: Vector2D) -> Circumference:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> Circumference:
        return self + other

    def __isub__(self, other: Vector2D) -> Circumference:
        return self - other


class Circle(Circumference):

    @property
    def circumference(self) -> Circumference:
        return Circumference(self.center, self.radius)

    @property
    @reduct_num
    def area(self) -> number:
        return pi * self.radius**2

    def __contains__(self, item: Point2D) -> bool:
        return LineSegment2D(self.center, item).length <= self.radius


class Arc:
    def __init__(
            self,
            circumference: Circumference | Circle,
            start: number,
            end: number,
            angle_unit: AngleUnitBase = AngleUnits.RADIANT
    ):
        self._circumference = circumference if not isinstance(circumference, Circle) else circumference.circumference
        self._angle_unit = angle_unit
        raise_if(
            ValueError("Arc start is greater than or equal to Arc end plus full rotation."),
            start >= end + angle_unit.full_rotation
        )
        raise_if(
            ValueError("Neither start nor end can be greater than or equal to double angle unit's full rotation"),
            start >= angle_unit.full_rotation or end >= 2*angle_unit.full_rotation
        )
        self._start = start
        self._end = end

    @property
    @exclusive_to('Arc')
    def sector(self) -> Sector:
        return Sector(self.circumference, self.start, self.end, self.angle_unit)

    @property
    @from_private_attr
    def circumference(self) -> Circumference: pass  # NoQA

    @property
    def circle(self) -> Circle:
        return self.circumference.circle

    @property
    @reduct_num
    @from_private_attr
    def start(self) -> number: pass  # NoQA

    @property
    @reduct_num
    @from_private_attr
    def end(self) -> number: pass  # NoQA

    @property
    @from_private_attr
    def angle_unit(self) -> AngleUnitBase: pass  # NoQA

    @property
    @reduct_num
    def amplitude(self) -> number:
        return self.end - self.start

    @property
    @reduct_num
    def length(self) -> number:
        return self.circumference.perimeter * self.amplitude / self.angle_unit.full_rotation

    def __str__(self):
        return (f"{type(self).__name__}"
                f"(center={self.circumference.center}, "
                f"radius={self.circumference.radius}, "
                f"interval=[{self.start}, {self.end}])")

    def __contains__(self, item: Point2D):
        return self.start <= acos(item.x/self.circumference.radius) <= self.end \
            and item in self.circumference

    def __add__(self, other: Vector2D) -> Arc:
        return type(self)(self.circumference+other, self.start, self.end, self.angle_unit)

    def __sub__(self, other: Vector2D) -> Arc:
        return self + (-other)

    def __iadd__(self, other: Vector2D) -> Arc:
        return self + other

    def __isub__(self, other: Vector2D) -> Arc:
        return self - other


class Sector(Arc):

    @property
    @reduct_num
    def area(self) -> number:
        return self.circle.area * self.amplitude / self.angle_unit.full_rotation

    @property
    def arc(self) -> Arc:
        return Arc(self.circumference, self.start, self.end)

    def __contains__(self, item: Point2D):
        return self.start <= acos(item.x/self.circumference.radius) <= self.end \
            and item in self.circle

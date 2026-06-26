from __future__ import annotations
from .._utils import number, raise_if
from ..math_function import LinearFunc
from ..infinity import Infinity
from typing import Final


__all__: list[str] = ['Point2D', 'Line2D', 'LineSegment2D', "Ray2D", 'Vector2D']
# TODO: add:
#           circles
#           segment circles
#           regular polygons


class Point2D:

    def __init__(self, x: number = 0, y: number = 0) -> None:
        self.x = x
        self.y = y

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
        self.x -= other.x
        self.y -= other.y

    def __add__(self, other: Point2D | Vector2D) -> Vector2D | Point2D:
        if isinstance(other, Point2D):
            return Vector2D(-other, self)
        elif isinstance(other, Vector2D):
            return Point2D(self.x+other.x, self.y+other.y)

    def __iadd__(self, other: Vector2D):
        self.x += other.x
        self.y += other.y

    def __eq__(self, other: Point2D):
        return self.x == other.x and self.y == other.y


class Line2D:
    def __init__(self, slope: number, y_intercept: number):
        self.slope = slope
        self.y_intercept = y_intercept

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


class Ray2D(Line2D):
    def __init__(  # NoQA
            self,
            slope: number,
            p: Point2D,
            direction: bool = True,
            including: bool = True
    ):
        self.slope: number = slope
        self.edge: Point2D = p
        self.including: bool = including

        # True -> to +inf
        # False -> to -inf
        self.direction: bool = direction

    @property
    def line(self) -> Line2D:
        return Line2D(self.slope, self.y_intercept)

    @property
    def y_intercept(self) -> number:
        return self.edge.y - self.slope*self.edge.x

    @y_intercept.setter
    def y_intercept(self, value: number):
        self.slope = (self.edge.y - value)/self.edge.x

    def __str__(self):
        return (f'{self.line!s}, x ∈ '
                f'{f']{Infinity.negative:sp}' if not self.direction 
                    else f'{'[' if self.including else ']'}{self.edge.x}'}'
                f',{f'{Infinity.positive:sp}[' if self.direction
                    else f'{self.edge.x}{']' if self.including else '['}'}')

    def __contains__(self, item: Point2D):
        return (self.func(item.x) == item.y) and\
            (item.x.__ge__ if (self.direction == True) else item.x.__le__)(self.edge.x)  # NoQA


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
        return str(self) == str(other)

    def __ne__(self, other: LineSegment2D):
        return not self == other


class Vector2D:
    def __init__(self, v1: number | Point2D, v2: number | Point2D) -> None:  # NoQA
        raise_if(
            ValueError("For Vector initialization arguments v1 and v2 must share type."),
            type(v1) is not type(v2)
        )
        tp = type(v1)

        if tp == number:
            self.x = v1
            self.y = v2
        elif tp == Point2D:
            self.x = v2.x-v1.x
            self.y = v2.y-v1.y

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


@lambda _: _()
def _setup() -> None:
    Point2D._setup_origin()  # NoQA

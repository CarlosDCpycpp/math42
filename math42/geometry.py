from __future__ import annotations
from random import randint as _randint
from random import uniform as _randfloat
import math as _math
from ._utils import number
from ._utils.meta import MetaUninitializable


__all__: list[str] = ['Point', 'Line', 'Vector',
                      'Polygon', 'Circle', 'FractionCircle',
                      'Area', 'Volume', 'SurfaceArea','Pythagoras']


# UTILS
def _all_elements_same(lst) -> bool:
    return len(set(lst)) == 1 if lst else True


def _filter_list(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


class Point:
    """A 2-dimensional point.
    Argument:
        x;
        y.

    Properties:
        x;
        y."""

    total_points = 0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        Point.total_points += 1

# converters
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f'Point{str(self)}'

    def __bool__(self):
        if self.x > 0 and self.y > 0:
            return True
        else:
            return False

    def __neg__(self):
        return Point(-self.x, -self.y)

# operations DON'T REDEFINE
    def __add__(self, other: Point):
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __iadd__(self, other: Point):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Point):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __isub__(self, other: Point):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other: Point):
        return Point(x=self.x * other.x, y=self.y * other.y)

    def __imul__(self, other: Point):
        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other: Point):
        return Point(x=self.x / other.x, y=self.y / other.y)

    def __itruediv__(self, other: Point):
        self.x /= other.x
        self.y /= other.y
        return self

    def __floordiv__(self, other: Point):
        return Point(x=(self.x // other.x),
                     y=(self.y // other.y))

    def __ifloordiv__(self, other: Point):
        self.x //= other.x
        self.y //= other.y

    def __pow__(self, power: number | Point):
        if isinstance(power, Point):
            return Point(x=self.x ** power.x, y=self.y ** power.y)
        return Point(x=self.x ** power, y=self.y ** power)

    def __ipow__(self, power: number | Point):
        if isinstance(power, Point):
            self.x **= power.x
            self.y **= power.y
        else:
            self.x **= power
            self.y **= power
        return self

# comparators
    def __eq__(self, other):
        try:
            if self.x == other.x and self.y == other.y:
                return True
        except AttributeError:
            pass
        return False

    def __ne__(self, other):
        try:
            if self.x != other.x or self.y != other.y:
                return True
        except AttributeError:
            pass
        return False

    def __lt__(self, other: Point):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    def __le__(self, other: Point):
        if self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __gt__(self, other: Point):
        if self.x > other.x and self.y > other.y:
            return True
        return False

    def __ge__(self, other: Point):
        if self.x >= other.x and self.y >= other.y:
            return True
        return False

# other dunder s
    def __del__(self):
        Point.total_points -= 1

    def __getitem__(self, index: int):
        index = 0 if index == "x" else index
        index = 1 if index == "y" else index
        cords = [self.x, self.y]
        return cords[index]

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))

    def __contains__(self, item):
        cords = [self.x, self.y]
        return item in cords

    def __reversed__(self):
        return Point(self.y, self.x)

# REDEFINES
    def move(self, add_x, add_y):
        """Redefines the point by adding the arguments passed to the respective coordinates."""
        self.x = add_x
        self.y = add_y
        return self

# STATICS

    @staticmethod
    def average(*args):
        """Calculates the average point of the points that are passed as *args."""
        tot = Point(0, 0)
        n_args = len(args)

        for arg in args:
            if isinstance(arg, Point):
                tot.x += arg.x
                tot.y += arg.y
            else:
                exit('"media" func took a non Point as an arg')

        return Point(tot.x / n_args, tot.y / n_args)

# distances DON'T REDEFINE
    @staticmethod
    def distance_between(point_1, point_2) -> number:  #
        """Calculates the average distance between the points passed as *args."""
        return (float(point_1.x - point_2.x) ** 2.0 +
                float(point_1.y - point_2.y) ** 2.0) ** 0.5

    @staticmethod
    def distance_x(point_1, point_2) -> number:
        """Calculates the distance between the y of the points passed as *args."""
        return abs(point_1.x - point_2.x)

    @staticmethod
    def distance_y(point_1, point_2) -> number:
        """Calculates the distance between the x of the points passed as *args."""
        return abs(point_1.y - point_2.y)

    @staticmethod
    def distance_point(point, original_pnt):  # this return a Point
        """Calculates the distance between the x of the points passed as *args."""
        return point - original_pnt

    @staticmethod
    def slope(point_1, point_2) -> number:  # division by 0 error
        """Calculates the slope of 2 points that are passed as arguments."""
        support = 0
        while True:
            try:
                slope = (((point_2.y + support) - (point_1.y + support)) /
                         ((point_2.x + support) - (point_1.x + support)))
                break
            except ZeroDivisionError:
                support += 1
        return slope

    @staticmethod
    def algebraic_exp(point_1, point_2) -> str:  # this is useless
        # no idea why I added this
        """Returns a string with the algebraic expression of the linear function
        that the two points that are passed as *args compose.
        WARNING:
            This is limited to LINEAR FUNCTIONS."""
        slope = Point.slope(point_1, point_2)
        parte_num = point_1.y - point_1.x * slope
        if parte_num > 0:
            parte_num = "+ " + str(parte_num)
        elif parte_num == 0:
            parte_num = ""
        elif parte_num < 0:
            parte_num = f"- {abs(parte_num)}"
        return f"{slope}x {parte_num}"

    @staticmethod
    def rand(min_n=0, max_n=100, float_: bool = False):
        """Creates a random point.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_n, max_n, float_.
        The first two determine the limits of the random point's position,
        the third determines if the x and y can be floats."""
        if float_:
            return Point(_randfloat(min_n, max_n), _randfloat(min_n, max_n))
        else:
            return Point(_randint(min_n, max_n), _randint(min_n, max_n))


class Line:
    """A 2-dimensional line.
    Arguments:
        p1 (point 1);
        p2 (point 2).

    Properties:
        p1 (point 1);
        p2 (point 2);
        length."""

    total_lines = 0

    def __init__(self, p1: Point = Point(), p2: Point = Point(0, 1)):
        self.p1 = p1
        self.p2 = p2
        self.length = Point.distance_between(self.p1, self.p2)
        self.slope = Point.slope(self.p1, self.p2)

        Line.total_lines += 1

    def __str__(self):
        return f"({self.p1}; {self.p2})"

    def __repr__(self):
        return f'Line{str(self)}'

    def __bool__(self):
        if bool(self.p1) and bool(self.p2):
            return True
        return False

    def __neg__(self):
        return Line(-self.p1, -self.p2)

# operations DON'T REDEFINE
    def __add__(self, other: Line):
        return Line(self.p1 + other.p1, self.p2 + other.p2)

    def __iadd__(self, other: Line):
        self.p1 += other.p1
        self.p2 += other.p2
        return self

    def __sub__(self, other: Line):
        return Line(self.p1 - other.p1, self.p2 - other.p2)

    def __isub__(self, other: Line):
        self.p1 -= other.p1
        self.p2 -= other.p2
        return self

    def __mul__(self, other: Line):
        return Line(self.p1 * other.p1, self.p2 * other.p2)

    def __imul__(self, other: Line):
        self.p1 *= other.p1
        self.p2 *= other.p2
        return self

    def __truediv__(self, other: Line):
        return Line(self.p1 / other.p1, self.p2 / other.p2)

    def __itruediv__(self, other: Line):
        self.p1 /= other.p1
        self.p2 /= other.p2
        return self

    def __floordiv__(self, other: Line):
        return Line(p1=self.p1 // other.p1,
                    p2=self.p2 // other.p2,)

    def __ifloordiv__(self, other: Line):
        self.p1 //= other.p1
        self.p2 //= other.p2
        return self

    def __pow__(self, other: number | Line):
        return Line(self.p1 ** other.p1, self.p2 ** other.p2)

    def __ipow__(self, other: number | Line):
        self.p1 **= other.p1
        self.p2 **= other.p2
        return self

# comparators
    def __eq__(self, other):
        try:
            if self.p1 == other.p1 and self.p2 == other.p2:
                return True
        except AttributeError:
            pass
        return False

    def __ne__(self, other):
        try:
            if self.p1 != other.p1 or self.p2 != other.p2:
                return True
        except AttributeError:
            pass
        return False

    def __lt__(self, other: Line):
        if self.p1 < other.p1 and self.p2 < other.p2:
            return True
        return False

    def __le__(self, other: Line):
        if self.p1 <= other.p1 and self.p2 <= other.p2:
            return True
        return False

    def __gt__(self, other: Line):
        if self.p1 > other.p1 and self.p2 > other.p2:
            return True
        return False

    def __ge__(self, other: Line):
        if self.p1 >= other.p1 and self.p2 >= other.p2:
            return True
        return False

    # other dunder s
    def __del__(self):
        Line.total_lines -= 1

    def __hash__(self):
        return hash((self.p1, self.p2))

    def __getitem__(self, index):
        pnts = [self.p1, self.p2]
        return pnts[index]

    def __iter__(self):
        return iter((self.p1, self.p2))

    def __contains__(self, item):
        points = [self.p1, self.p2]
        return item in points

    def __reversed__(self):
        return Line(self.p2, self.p1)

# STATIC

    @staticmethod
    def average(*lines):
        """Calculates the average line between it's *args."""
        ps1 = []
        ps2 = []
        for line_ in lines:
            ps1.append(line_.p1)
            ps2.append(line_.p2)

        return Line(Point.average(*ps1), Point.average(*ps2))

    @staticmethod
    def avr_length(*lines) -> number:
        """Calculates the average length of the lines that are passed as *args."""
        tot = 0.0
        for line in lines:
            tot += line.lenght

        return tot / len(lines)

    @staticmethod
    def rand(min_=-100, max_=100, float_=False):
        """Returns a random line.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_n, max_n, float_.
        The first two determine the limits of the random line's position,
        the third determines if the points 1 and 2 can be floats."""
        return Line(Point.rand(min_, max_, float_), Point.rand(min_, max_, float_))

    @staticmethod
    def is_parallel(line1, line2) -> bool:
        """Checks if two lines are parallel"""
        if not isinstance(line1, Line) or not isinstance(line2, Line):
            raise TypeError(f": Either {line1} or {line2} (or both) is not a Line.")
        if line1.slope == line2.slope:
            return True
        return False


class Vector(Line):
    """A 2-dimensional vector.
    Arguments:
        p1 [int|float] (point 1);
        p2 [int|float] (point 2);
        strength.

    Properties:
        p1 (point 1);
        p2 (point 2);
        strength,
        shift (a point that can be added to other objects)"""
    total_vectors = 0

    def __init__(self, line, strength=1.0):
        Vector.total_vectors += 1

        if isinstance(line, Line):
            p1 = line.p1
            p2 = line.p2
        elif isinstance(line, list):
            p1 = line[0]
            p2 = line[1]
        else:
            raise ValueError

        super().__init__(p1, p2)
        self.line = Line(p1, p2)
        self.strength = strength

        self.shift = self.p2 - self.p1

    def __str__(self):
        return f'({str(self.line)}; Strength: {self.strength})'

    def __repr__(self):
        return f'Vector{str(self)}'

    def __neg__(self):
        return Vector(-self.line, strength=-self.strength)

    def __del__(self):
        Vector.total_vectors -= 1

    def __call__(self, other, sum_=True):
        if sum_:
            return other + self
        else:
            return other - self

# reverse operating
    # I'm going to just leave it with only radd and rsub
    # since it's what makes the most sense

    def __radd__(self, other: Point|Line|Polygon|Circle|FractionCircle):
        if isinstance(other, Polygon):
            z = []
            for pnt in other.points:
                z.append(pnt + self.shift)
            return Polygon(z)
        if isinstance(other, Circle):
            center = other.center + self.shift
            edge = other.edge + self.shift
            return Circle(center=center, edge=edge)
        if isinstance(other, Point):
            return other + self.shift
        if isinstance(other, Line):
            return Line(p1=other.p1+self.shift, p2=other.p2+self.shift)

    def __rsub__(self, other: Point|Line|Polygon|Circle|FractionCircle):
        return other + -self

# other dunder s

    def __hash__(self):
        return hash((self.line, self.strength))

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100,
              min_strength=-50, max_strength=50,
              line_float=False, strength_float=False):
        """Creates a random vector.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_n, max_n, min_strength, max_strength, line_float_, strength_float.
        The first two determine the limits of the random vector's position,
        the third and fourth determine the limit the strength,
        the last two determine if the line and strength can be floats (both are by default false)."""
        l_ = Line.rand(min_, max_, line_float)
        if strength_float:
            s = _randfloat(min_strength, max_strength)
        else:
            s = _randint(min_strength, max_strength)
        return Vector(l_, s)


class Polygon:
    """A polygon.
    Arguments:
        points [list].

    Properties:
        points;
        lines;
        perimeter;
        sum_inner_angles;
        angles;
        area;
        type_."""

    total_polygons = 0

    def __init__(self, points):

        Polygon.total_polygons += 1

        self.points = _filter_list(points)

        self.lines = []
        self.lines.append(Line(points[-1], points[0]))
        for point in points:
            if point == self.points[-1]:
                continue
            nx_p = self.points[self.points.index(point) + 1]
            self.lines.append(Line(point, nx_p))

        self.lines_len = []
        self.perimeter = 0
        for line in self.lines:
            self.lines_len.append(line.length)
            self.perimeter += line.length

        self.n_lines = len(self.lines)

        pass  # angles
        self.sum_inner_angles = (self.n_lines - 2) * 180
        #
        # self.angles = []
        # for i in range(self.n_lines):
        #     p1 = self.points[i]
        #     p2 = self.points[(i + 1) % self.n_lines]
        #     p3 = self.points[(i + 2) % self.n_lines]
        #
        #     # Vectors
        #     v1 = (p2.x - p1.x, p2.y - p1.y)
        #     v2 = (p3.x - p2.x, p3.y - p2.y)
        #
        #     # Dot product and magnitudes
        #     dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        #     mag_v1 = _math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        #     mag_v2 = _math.sqrt(v2[0] ** 2 + v2[1] ** 2)
        #
        #     # Angle in radians
        #     angle_rad = _math.acos(dot_product / (mag_v1 * mag_v2))
        #     # Convert to degrees
        #     angle_deg = _math.degrees(angle_rad)
        #     self.angles.append(angle_deg)

        # area
        self.area = 0.0  # I haven't learnt this yet so GPT made it
        for i in range(self.n_lines):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i + 1) % self.n_lines].x, self.points[(i + 1) % self.n_lines].y
            self.area += x1 * y2 - x2 * y1
        self.area = abs(self.area) / 2.0

        # regular
        z = []
        for line in self.lines:
            z.append(line.length)

        if _all_elements_same(self.angles) and _all_elements_same(z):
            self.is_regular = True
        else:
            self.is_regular = False

        # type_
        polygon_names = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon",
            11: "Hendecagon",
            12: "Dodecagon"
        }

        polygon_name = polygon_names.get(self.n_lines, "Unknown")

        if self.n_lines == 3:
            if all(_math.isclose(angle, 60, abs_tol=1e-6) for angle in self.angles):
                self.type_ = ["Triangle", "Equilateral"]
            elif any(_math.isclose(angle, 90, abs_tol=1e-6) for angle in self.angles):
                self.type_ = ["Triangle", "Right"]
            elif len(set(self.angles)) == 2:
                self.type_ = ["Triangle", "Isosceles"]
            else:
                self.type_ = ["Triangle", "Scalene"]

        # kite not added (yet)
        elif self.n_lines == 4:
            if any(_math.isclose(self.angles[i], 90, abs_tol=1e-6) for i in range(4)):
                if _all_elements_same(self.angles) and self.angles[0] == 90:
                    if _all_elements_same(self.lines_len):
                        self.type_ = "Square"
                    else:
                        self.type_ = "Rectangle"
                else:
                    self.type_ = "Right Trapezoid"
            else:
                if _all_elements_same(self.angles[1:3]) and len(set(self.angles)) == 3:
                    self.type_ = "Isosceles Trapezoid"
                elif _all_elements_same(self.lines_len):
                    self.type_ = "Rhombus"
                elif self.angles[0] == self.angles[2] and self.angles[1] == self.angles[3]:
                    self.type_ = "Parallelogram"
                else:
                    self.type_ = "Trapezoid"

        elif self.is_regular:
            if self.n_lines == 4:
                if _all_elements_same(self.angles) and self.angles[0] == 90:
                    self.type_ = "Square"
                else:
                    self.type_ = "Rhombus"
            else:
                self.type_ = polygon_name

        else:
            self.type_ = polygon_name

    @property
    def angles(self):
        angles = []
        for i in range(self.n_lines):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % self.n_lines]
            p3 = self.points[(i + 2) % self.n_lines]

            v1 = (p2.x - p1.x, p2.y - p1.y)
            v2 = (p3.x - p2.x, p3.y - p2.y)

            dot_product = v1[0] * v2[0] + v1[1] * v2[1]
            mag_v1 = _math.sqrt(v1[0] ** 2 + v1[1] ** 2)
            mag_v2 = _math.sqrt(v2[0] ** 2 + v2[1] ** 2)

            angle_rad = _math.acos(dot_product / (mag_v1 * mag_v2))
            angle_deg = _math.degrees(angle_rad)
            angles.append(angle_deg)
        return angles

# converters
    def __str__(self):
        str_ = ""
        for i in self.points:
            str_ += f"{i}; "
        str_ = str_[:-2]
        return f'({str_})'

    def __repr__(self):
        return f'Polygon{str(self)}'

    def __bool__(self):
        for point in self.points:
            if not point:
                return False
        return True

    def __neg__(self):
        n_pnts = []
        for pnt in self.points:
            n_pnts.append(-pnt)
        return Polygon(n_pnts)

# comparators
    # I'm comparing AREAS
    def __eq__(self, other):
        try:
            if self.points == other.points:
                return True
        except AttributeError:
            pass
        return False

    def __ne__(self, other):
        try:
            if self.points != other.points:
                return True
        except AttributeError:
            pass
        return False

    def __lt__(self, other: Polygon|Circle|FractionCircle):
        if self.area < other.area:
            return True
        return False

    def __le__(self, other: Polygon|Circle|FractionCircle):
        if self.area <= other.area:
            return True
        return False

    def __gt__(self, other: Polygon|Circle|FractionCircle):
        if self.area > other.area:
            return True
        return False

    def __ge__(self, other: Polygon|Circle|FractionCircle):
        if self.area >= other.area:
            return True
        return False

# other dunder s
    def __del__(self):
        Polygon.total_polygons -= 1

    def __getitem__(self, index_):  # type_ can be "line"
        type_ = "p"
        index = None

        if isinstance(index_, tuple):
            flag1 = False
            flag2 = False
            for i in index_:
                if isinstance(i, str):
                    type_ = i
                    flag1 = True
                elif isinstance(i, int):
                    index = i
                    flag2 = True

            if not flag1 or not flag2:
                raise IndexError

        elif isinstance(index_, int):
            index = index_
            type_ = "p"

        else:
            raise IndexError

        type_ = type_.lower()
        if type_ == "point" or type_ == "pnt" or type_ == "p":
            result = self.points[index]
        elif type_ == "line" or type_ == "ln" or type_ == "l":
            result = self.lines[index]
        else:
            raise ValueError(f"Invalid Type: {type_}")
        return result

    def __iter__(self):
        return iter(self.points)

    def __contains__(self, other):
        if isinstance(other, Point):
            return other in self.points
        elif isinstance(other, Line):
            return other in self.lines
        elif isinstance(other, int):
            cords = []
            for point in self.points:
                cords.append(point.x)
                cords.append(point.y)
            return other in cords

    def __reversed__(self):
        return Polygon(self.points[::-1])

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100, min_points=3, max_points=12, float_=False):
        """Creates a random polygon.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_, max_, min_points, max_points, float_.
        The first two determine the limits of the random polygon's position,
        the third and fourth determine the bottom and upper limits of the number of points,
        the last determines if the points can be floats (by default is false)."""
        pnts = []
        for i in range(_randint(min_points, max_points)):
            pnts.append(Point.rand(min_, max_, float_))
        return Polygon(pnts)


class Circle:
    """A circle.

    Arguments:
        center;
        edge;
        radius.
    At least two arguments have to be given, since with two the initializer determines the one that remains.

    Properties:
        center;
        edge;
        radius;
        diameter;
        circumference;
        area;
        all_points (there's a point for each degree and, they are edge points of the circle at their angle)."""

    total_circles = 0

    def __init__(self, center: Point = Point(),
                 edge: Point = Point(), radius=None):
        Circle.total_circles += 1

        self.center = center
        self.edge = edge
        if radius is None:
            self.radius = Line(center, edge)
        elif isinstance(radius, Line):
            self.radius = radius
        elif isinstance(radius, (int, float)):
            self.radius = Line(center, Point(center.x, center.y + radius))
        else:
            self.radius = Line(self.center, self.edge)

        if self.edge == Point():
            self.edge = self.radius[1]
        if self.center == Point():
            self.center = self.radius[0]

        self.diameter = self.radius.length * 2

        self.all_points = []
        for angle in range(0, 360):
            x = round(self.center.x + self.radius.length * _math.cos(_math.radians(angle)), 5)
            y = round(self.center.y + self.radius.length * _math.sin(_math.radians(angle)), 5)
            self.all_points.append(Point(x, y))

        # area
        self.area = _math.pi * self.radius.length ** 2

        # perimeter
        self.circumference = 2 * _math.pi * self.radius.length

# converters
    def __str__(self):
        return f"(Center: {self.center}; Radius: {self.radius.length})"

    def __repr__(self):
        return f'Circle{str(self)}'

    def __bool__(self):
        if not self.center:
            return False
        return True

    def __neg__(self):
        return Circle(-self.center, -self.edge, -self.radius)

# operators

# comparators
    def __eq__(self, other):
        if isinstance(other, Circle):
            if other.center == self.center and other.radius == self.radius:
                return True
            return False
        return False

    def __ne__(self, other):
        if other == self:
            return False
        return True

    def __le__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area <= other.area:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area < other.area:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area >= other.area:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area > other.area:
                return True
        return False

# other dunder s
    def __del__(self):
        Circle.total_circles -= 1

    def __getitem__(self, index):
        if index == 360:
            index = 0
        if index < 0:
            index += 360
        return self.all_points[index]

    def __iter__(self):
        return iter(self.all_points)

    def __contains__(self, other):
        if isinstance(other, Point):
            if other in self.all_points:
                return True
            return False
        if isinstance(other, Line):
            flag1 = False
            flag2 = False
            for i in other:
                if i == self.center:
                    flag1 = True
                elif i in self.all_points:
                    flag2 = True
            if flag1 and flag2:
                return True
            return False

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100, float_=False):
        """Creates a random circle.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_, max_, float_.
        The first two determine the limits of the random circle's position,
        the last one determines if the points can be floats (by default is false)."""
        center = Point.rand(min_, max_, float_)
        if float_:
            radius = Line(center, Point.rand())
        else:
            radius = Line(center, Point.rand())
        edge = Point(radius[1][0], radius[1][0])

        return Circle(center=center, radius=radius, edge=edge)


class FractionCircle(Circle):
    """A fraction of a circle (e.g. a half-circle).

    Arguments:
        center;
        edge;
        radius;
        percentage.
    At least two of the first three arguments have to be given,
    since with two the initializer determines the one that remains.
    Percentages are, by default, 50%.

    Properties:
        center;
        edge;
        radius;
        diameter;
        circumference;
        area;
        all_points (there's a point for each degree and, they are edge points of the circle at their angle);
        percentage."""

    def __init__(self, center: Point = Point(),
                 edge: Point = Point(), radius=None,
                 percentage: int = 50):
        super().__init__(center, edge, radius)

        self.full_circle = Circle(center, edge, radius)

        self.percentage = percentage / 100
        self.area *= self.percentage
        self.circumference *= self.percentage

        self.all_points = []
        i = round(360*self.percentage)
        for angle in range(0, i):
            x = round(self.center.x + self.radius.length * _math.cos(_math.radians(angle)), 5)
            y = round(self.center.y + self.radius.length * _math.sin(_math.radians(angle)), 5)
            self.all_points.append(Point(x, y))

    def __str__(self):
        return f"({self.full_circle}; Percentage: {self.percentage * 100})"

    def __repr__(self):
        return f'FractionCircle{str(self)}'

    def __eq__(self, other):
        if (isinstance(other, FractionCircle) and
                self.full_circle == other.full_circle and
                self.percentage == other.percentage):
            return True
        return False

    def __ne__(self, other):
        if isinstance(other, FractionCircle) and self == other:
            return False
        return True

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100, float_=False,
              perc_min=10, perc_max=90):
        """Creates a random circle.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_, max_, float_, perc_min, perc_max.
        The first two determine the limits of the random circle's position,
        the third one determines if the points can be floats (by default is false),
        the last two determine the limits of the percentage of the circle (by default, they are 10 and 90, respectively)
        """
        c_ = Circle.rand(min_, max_, float_)
        p = _randint(perc_min, perc_max)
        return FractionCircle(center=c_.center, edge=c_.edge,
                              radius=c_.radius, percentage=p)


# STATIC CLASSES
# these are not finished
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
        return _math.pi * radius**2


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
        return (4/3) * _math.pi * radius**3

    @staticmethod
    def cylinder(radius: number, height: number) -> number:
        return _math.pi * radius**2 * height

    @staticmethod
    def cone(radius: number, height: number) -> number:
        return (1/3) * _math.pi * radius**2 * height


class SurfaceArea(metaclass=MetaUninitializable):

    @staticmethod
    def sphere(radius: number) -> number:
        return 4 * _math.pi * radius**2

    @staticmethod
    def cylinder(radius: number, height: number) -> number:
        return 2 * _math.pi * radius * (radius + height)

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

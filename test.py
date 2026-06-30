from math42.geometry import *
from math import pi

cl = Circle(Point2D.ORIGIN, 5.0)
cf = cl.circumference

a = Arc(cf, 0, 0.25*pi)

print(a.sector)

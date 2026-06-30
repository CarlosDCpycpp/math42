from ._utils import number
from .constants import Const

__all__: list[str] = ['speed', 'time', 'distance', 'force', 'weight', 'space_travelled']


def speed(distance: number, time: number) -> number:  # NoQA
    """Calculates the speed.
    Takes distance and time as arguments."""
    return distance / time


def time(distance: number, speed: number) -> number:  # NoQA
    """Calculates the time.
    Takes distance and speed as arguments."""
    return distance / speed


def distance(speed: number, time: number) -> number:  # NoQA
    """Calculates the distance.
    Takes speed and time as arguments."""
    return speed * time


def force(mass: number, acceleration: number) -> number:
    """Calculates the force.
    Takes mass and acceleration as arguments."""
    return mass * acceleration


def weight(mass: number, gravity: number = Const.GRAVITY_ON_EARTH) -> number:
    """Calculates the weight.
    Takes mass and gravity as arguments.
    (gravity is, by default, 9.8, however can be altered by being passed as an argument.)"""
    return mass * gravity


def space_travelled(starting_pos: number, ending_pos: number) -> number:
    """Calculates the space travelled.
    Takes the starting position and ending position as arguments."""
    return abs(starting_pos - ending_pos)

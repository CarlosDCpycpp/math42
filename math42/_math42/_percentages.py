from .._utils import number
from .._utils.meta import MetaUninitializable
from ._funcs import rule_of_3


__all__: list[str] = ['Percentage']


class Percentage(metaclass=MetaUninitializable):

    @classmethod
    def find(cls, fraction: number, whole: number) -> number:
        """Return the percentage of the fraction in relation to the whole (both are passed as arguments)"""
        return rule_of_3(whole, fraction, 100)

    @classmethod
    def find_increase(cls, new_value: number, original_value: number) -> number:
        """Return the percentage increase between 2 values that are passed as arguments."""
        increase = new_value - original_value
        percentage_increase = cls.find(original_value, increase)
        return round(percentage_increase, 2)

    @classmethod
    def from_fraction(cls, numerator: number, denominator: number) -> number:
        """Converts a fraction to percentage.
        This is done by taking the denominator as the whole and the numerator as the fraction."""
        return cls.find(denominator, numerator)

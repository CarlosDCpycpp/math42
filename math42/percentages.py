from ._utils import number
from ._others import rule_of_3


__all__: list[str] = ['find_perc', 'find_increase', 'fraction_to_perc']


def find_perc(fraction: number, whole: number) -> number:
    """Return the percentage of the fraction in relation to the whole (both are passed as arguments)"""
    return rule_of_3(whole, fraction, 100)


def find_increase(new_value: number, original_value: number) -> number:
    """Return the percentage increase between 2 values that are passed as arguments."""
    increase = new_value - original_value
    percentage_increase = find_perc(original_value, increase)
    return round(percentage_increase, 2)


def fraction_to_perc(numerator: number, denominator: number) -> number:
    """Converts a fraction to percentage.
    This is done by taking the denominator as the whole and the numerator as the fraction."""
    return find_perc(denominator, numerator)

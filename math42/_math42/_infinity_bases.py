from typing import final
from .._utils.meta import meta_limit


@final
class InfinityBases(metaclass=(meta_limit(2))):

    def __init__(self, pos_neg_spec: bool):
        self._pos: bool = pos_neg_spec

    def __repr__(self):
        return f'{self!s}: pos_neg_spec: {(True if self._pos else False)!s}'

    def __str__(self):
        return f'{'' if self._pos else 'negative '}infinity'

    def __format__(self, format_spec: str):
        match spec := format_spec.lower().strip():
            case 'word' | 'w':
                return 'Infinity' if self._pos else '-Infinity'

            case 'symbol':
                return '∞' if self._pos else '-∞'

            case 'word_sp' | 'wsp':
                return '+Infinity' if self._pos else self.__format__('word')

            case 'words' | 'ws':
                return 'Positive Infinity' if self._pos else 'Negative Infinity'

            case 'words_sp' | 'wssp':  # NOQA
                return 'Positive ∞' if self._pos else 'Negative ∞'

            case 'sp':
                return '+∞' if self._pos else self.__str__()

            case '_':
                return f'{'positive' if self._pos else 'negative'} infinity'

            case '':
                return '(no specifier passed)'

            case _:
                return f'Unknown specifier: [{spec}]'

    def __bool__(self):
        return self._pos

    # comparators
    def __eq__(self, other):
        return isinstance(other, InfinityBases) and self._pos == other._pos

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return (self._pos and not other._pos) if isinstance(other, InfinityBases) else self._pos

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return (not self._pos and other._pos) if isinstance(other, InfinityBases) else not self._pos

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    # operators
    def __add__(self, other):
        if isinstance(other, InfinityBases):
            if self._pos and other._pos:
                return InfinityBases(True)
            elif not self._pos and not other._pos:
                return InfinityBases(False)
            else:
                return InfinityBases(True)
        return self

    def __sub__(self, other):
        if isinstance(other, InfinityBases):
            if self._pos and other._pos:
                return float('nan')
            elif self._pos and not other._pos:
                return InfinityBases(True)
            elif not self._pos and self._pos:
                return InfinityBases(False)
            else:
                return float('nan')
        return self

    def __mul__(self, other):
        if isinstance(other, InfinityBases):
            if self._pos and other._pos:
                return InfinityBases(True)
            elif self._pos and not other._pos:
                return InfinityBases(False)
            elif not self._pos and other._pos:
                return InfinityBases(False)
            else:
                return InfinityBases(True)
        return self if other > 0 else InfinityBases(False)

    def __truediv__(self, other):
        if isinstance(other, InfinityBases):
            if self._pos and other._pos:
                return float('nan')
            elif self._pos and not other._pos:
                return InfinityBases(True)
            elif not self._pos and other._pos:
                return InfinityBases(False)
            else:
                return float('nan')
        return InfinityBases(True) if other > 0 else InfinityBases(False)

    def __floordiv__(self, other):
        if isinstance(other, InfinityBases):
            if self._pos and other._pos:
                return InfinityBases(True)
            elif self._pos and not other._pos:
                return InfinityBases(False)
            elif not self._pos and other._pos:
                return InfinityBases(False)
            else:
                return InfinityBases(True)
        return InfinityBases(True) if other < 0 else InfinityBases(False)

    def __neg__(self):
        return InfinityBases(not self._pos)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return InfinityBases(False) if isinstance(other, InfinityBases) and other._pos else self.__neg__()

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return InfinityBases(False) if isinstance(other, InfinityBases) and other._pos else self.__neg__()

    def __rfloordiv__(self, other):
        return InfinityBases(False) if isinstance(other, InfinityBases) and other._pos else self.__neg__()

    # other dunders
    def __abs__(self):
        return InfinityBases(True)

    def __iter__(self):
        i = 0
        while True:
            yield i

            i += 1 if self._pos else -1

    def __contains__(self, item):
        if self._pos and item > 0:
            return True
        elif not self._pos and item < 0:
            return True
        return False

    def __hash__(self):
        return hash(f'{self:_}')

    def __instancecheck__(self, instance) -> bool:
        return True if instance in [float, InfinityBases] else False

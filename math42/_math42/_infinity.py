from .._math42._infinity_bases import InfinityBases

from typing import (
    final,
    Final
)
from .._utils.meta import MetaUninitializable


__all__: list[str] = ['Infinity']


@final
class Infinity(metaclass=MetaUninitializable):
    positive: Final[InfinityBases] = InfinityBases(True)
    negative: Final[InfinityBases] = InfinityBases(False)

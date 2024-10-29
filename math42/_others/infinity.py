from math42._bases.infinity_bases import InfinityBases

from typing import (
    final,
    Final
)
from math42._utils.init_control import MetaUninitializable


__all__: list[str] = ['Infinity']


@final
class Infinity(metaclass=MetaUninitializable):
    positive: Final[InfinityBases] = InfinityBases(True)
    negative: Final[InfinityBases] = InfinityBases(False)

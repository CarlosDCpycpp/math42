from typing import Generator
from ._math42._infinity_bases import InfinityBases  # NOQA
from ._math42._infinity import Infinity


__all__: list[str] = ['NumberRange']


class NumberRange:
    def __init__(self,
                 less_than: int | None, more_than: int | None,
                 jump: int | list[int] | None = None):

        assert not (less_than is None and more_than is None), (
            'Parameters "less_than" and "more_than" must not both be None')

        if isinstance(less_than, int) and isinstance(more_than, int):
            assert more_than < less_than, 'Parameter "less_than" must be more than "more_than"'
            assert more_than != less_than, 'Parameters "less_than" and "more_than" must not be equal'

        self.less_than: int | None = less_than
        self.more_than: int | None = more_than

        self.jump: int | list[int] | None = jump

    @property
    def __less_than_check(self) -> bool:
        return False if self.less_than is None else True

    @property
    def __more_than_check(self) -> bool:
        return False if self.more_than is None else True

    @property
    def __jump_check(self) -> bool:
        return False if self.jump is None else True

    @property
    def __iter(self) -> Generator:
        return self.__iter__()

    def __iter__(self) -> Generator:

        def _jump_gen() -> Generator | None:
            if isinstance(self.jump, list):
                while True:
                    for j in self.jump:
                        yield j
            return

        jumps = _jump_gen()
        flag = False

        if self.__more_than_check and self.__less_than_check:
            i = self.more_than
            while i < (self.less_than+1):
                if flag:
                    yield i
                else:
                    flag = True
                if self.__jump_check:
                    if isinstance(self.jump, int):
                        i += self.jump
                    elif isinstance(self.jump, list):
                        i += next(jumps)
                else:
                    i += 1

        elif self.__less_than_check:
            i = (self.less_than+1)
            while True:
                if flag:
                    yield i
                else:
                    flag = True
                if self.__jump_check:
                    if isinstance(self.jump, int):
                        i -= self.jump
                    elif isinstance(self.jump, list):
                        i -= next(jumps)
                else:
                    i -= 1

        elif self.__more_than_check:
            i = self.more_than
            while True:
                if flag:
                    yield i
                else:
                    flag = True
                if self.__jump_check:
                    if isinstance(self.jump, int):
                        i += self.jump
                    elif isinstance(self.jump, list):
                        i += next(jumps)
                else:
                    i += 1

    def __contains__(self, item: int) -> bool:
        if item == self.more_than or item == self.less_than:
            return False

        if self.__more_than_check and self.__less_than_check:
            for i in self:
                if i == item:
                    return True
                if i > self.less_than:
                    break

        elif self.__less_than_check:
            for i in self:
                if i == item:
                    return True
                if i < item:
                    break

        elif self.__more_than_check:
            for i in self:
                if i == item:
                    return True
                if i > item:
                    break
        return False

    def __next__(self):
        return next(self.__iter)

    def __str__(self):
        range_desc = []

        if self.__more_than_check:
            range_desc.append(f"more than: {self.more_than}")

        if self.__less_than_check:
            range_desc.append(f"less than: {self.less_than}")

        if self.__jump_check:
            jump_desc = ''
            if isinstance(self.jump, int):
                jump_desc = f"jump: {self.jump}"
            elif isinstance(self.jump, list):
                if len(self.jump) == 1:
                    jump_desc = f"jump: {self.jump[0]}"
                else:
                    jump_desc = f"jumps: {self.jump}"

            range_desc.append(jump_desc)

        return "NumberContainer: " + "; ".join(range_desc)

    @property
    def length(self) -> int | InfinityBases:
        if not self.__more_than_check or not self.__less_than_check:
            return Infinity.positive
        i = 0
        for _ in self:
            i += 1
        return i

    @property
    def min(self):
        if not self.__more_than_check:
            return Infinity.negative
        for result in self:
            return result

    @property
    def max(self):
        if not self.__less_than_check:
            return Infinity.positive
        elif not self.__more_than_check:
            return self.less_than
        result = None
        for i in self:
            result = i
        return result

    @property
    def start(self):
        for i in self:
            return i

    @property
    def finish(self):
        return None if isinstance(self.max, InfinityBases) else self.max

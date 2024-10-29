from functools import cache
from copy import copy


__all__: list[str] = ['MetaUninitializable', 'meta_limit']


class InitializationError(Exception):
    pass


class MetaUninitializable(type):
    def __call__(cls):
        raise InitializationError(f'The class "{cls.__name__}" is not supposed to be initialized.')


@cache
def meta_limit(limit: int):
    class _MetaLimit(type):
        _limit_control = 0

        def __call__(cls, *args, **kwargs):
            if cls._limit_control >= limit:
                raise InitializationError(f'Class "{cls.__name__}" was over-initialized; limit: {limit}.')
            instance = super().__call__(*args, **kwargs)
            cls._limit_control += 1
            return instance

    return copy(_MetaLimit)

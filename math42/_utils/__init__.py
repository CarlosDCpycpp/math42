from typing import Any, Callable, NoReturn


number = int | float


def include(*errors: type[Exception], value: Any = None):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(errors):
                return value
        return wrapper
    return decorator


class InvalidLogicException(Exception): pass


def raise_if(error: type[Exception] | Exception, *conds, logic_spec: str = 'and') -> NoReturn | None:

    logic_spec = logic_spec.lower().strip()

    try:
        logic: bool = {
            'and': all,
            'or': any,
            'xor': lambda cs: sum(bool(c) for c in cs) % 2 == 1
        }.get(logic_spec, None)(conds)
    except TypeError:
        raise InvalidLogicException(
            f'Invalid specifier "{logic_spec}" for function "raise_if"; the specifier must be either "and", "or" or "xor".')

    if logic:
        raise error if isinstance(error, Exception) else error()


def _all_elements_same(lst) -> bool:
    return len(set(lst)) == 1 if lst else True


def _remove_dups(lst: list) -> list:
    seen = set()
    result = []
    try:
        for item in lst:
            if item not in seen:
                result.append(item)
                seen.add(item)
        return result
    except TypeError:
        raise TypeError("All elements on target list must be hashable.")


class HashEqualComparable:
    def __eq__(self, other):
        return (hash(self) == hash(other)) and (type(self) is type(other))

    def __ne__(self, other):
        return not self.__eq__(other)
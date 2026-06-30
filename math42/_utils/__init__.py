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


def reduct_num(nf: number | Callable) -> int | float | Callable:
    if isinstance(nf, Callable):
        def wrapper(*args, **kwargs) -> number:
            return reduct_num(nf(*args, **kwargs))
        return wrapper

    if int(nf) == float(nf):
        return int(nf)
    return float(nf)


def from_private_attr(f: Callable):
    def wrapper(self: object) -> Any:
        return self.__getattribute__(f"_{f.__name__}")
    return wrapper


def exclusive_to(cls_name: str):
    def decorator(meth: Callable):
        def wrapper(*args, **kwargs) -> Any:
            raise_if(
                TypeError(f"The {meth.__name__} method is exclusive to the {cls_name} class."),
                type(args[0]).__name__ != cls_name
            )
            return meth(*args, **kwargs)
        return wrapper
    return decorator

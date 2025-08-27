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


def raise_if(error: type[Exception] | Exception, *conds, logic_spec: str = 'and') -> NoReturn | None:

    logic_spec = logic_spec.lower().strip()

    logic: bool = {
        'and': all,
        'or': any,
        'xor': lambda *cs: sum(bool(c) for c in cs) % 2 == 1
    }.get(logic_spec, None)(*conds)

    if logic is None:
        raise ValueError(f'Invalid specifier "{logic_spec}" for function "raise_if"; the specifier must be either "and", "or" or "xor".')

    if logic:
        raise error if isinstance(error, Exception) else error()

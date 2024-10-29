from typing import Any, Callable


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

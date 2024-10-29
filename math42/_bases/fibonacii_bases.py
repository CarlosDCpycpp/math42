from collections.abc import Generator


def base_fibonacci_generator() -> Generator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

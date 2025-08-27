from .._math42 import is_prime, Fibonacci
from typing import Generator


print('\033[31mI WARNED YOU\033[0m')


def prime_gen() -> Generator[int, None, None]:
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def get_primes() -> None:
    primes = prime_gen()
    with open('primes.txt', 'a') as file:
        for num in primes:
            print(num)
            file.write(f'{num}\n')


def check_primes() -> None:
    with open('primes.txt', 'r') as file:

        print('Creating prime list')
        primes: list = [int(i) for i in file.read().split('\n') if i != '']
        print('Prime list created.')

        for num in primes:
            print(f'Checking {num}: ...', end='')
            if not is_prime(num):
                print(f'\rChecking {num}: {False}.')
                break
            print(f'\rChecking {num}: {True}.')

        else:
            print(f'All numbers checked were primes; True.')


def fib() -> None:
    fib_gen = Fibonacci.generator()
    with open('fibonacci', 'a') as file:
        for num in fib_gen:
            print(num)
            file.write(f'{num}\n')

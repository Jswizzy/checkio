from itertools import chain

from math import sqrt


def is_prime(n):
    n = abs(n)
    return False if n % 2 == 0 and n > 2 else all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def factors(n):
    step = 2 if n % 2 else 1
    return [[i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0]


# prime factors
def fta(n):
    primes = []
    div = 2
    i = 2 if n % 2 else 1
    # div * div >= n also would work
    while not is_prime(n):
        if n % div:
            div += i
        else:
            n //= div
            primes.append(div)
    primes.append(abs(int(n)))
    if n < 0:
        primes.append(-1)
    return primes


# LCM

# GCD


if __name__ == '__main__':
    print("tests\n")

    sixty = factors(20)
    print(sixty)

    print(sorted(chain(*sixty)))

    print(fta(20))

    print(max(len([100]), len([2, 3, 4, 5])))

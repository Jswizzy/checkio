from itertools import chain

from math import sqrt


def is_prime(n):
    n = abs(n)
    return False if n % 2 == 0 and n > 2 else all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def fta(n):
    primes = []
    while not is_prime(n):
        div = 2
        while n % div:
            div += 1
        n = n / div
        primes.append(div)
    primes.append(abs(int(n)))
    if n < 0:
        primes.append(-1)
    return primes


def checkio(number):
    result = fta(number) if not is_prime(number) else 0

    if result:
        for number in list(result):
            if number > 10:
                return 0

    return int("".join(map(str, result))) if result else 0

if __name__ == '__main__':
    checkio(125)


    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(125) == 555, '555'

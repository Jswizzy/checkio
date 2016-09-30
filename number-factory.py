from functools import reduce
from math import sqrt


def is_prime(n):
    return False if n % 2 == 0 and n > 2 else all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


def lowest_factors(n):

    ar = sorted(list(factors(n)))

    mid = len(ar) // 2

    ar = ar[mid - 1:mid + 1]

    for num in ar:
        if not num == is_prime(num) and num >= 10 and num > 2:
            num = lowest_factors(num)

    if ar.count(1) > 1:
        return [0]

    print(ar)

    return ar if all(list(map(lambda x: x < 10, ar)))\
        else [0]


def checkio(number):
    if not is_prime(number):

        # print(lowest_factors(number))
        # print("".join(list(map(str, lowest_factors(number)))))
        return int("".join(list(map(str, lowest_factors(number)))))
    return 0

if __name__ == '__main__':

    print(sorted(list(factors(125))))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(125) == 555, '555'

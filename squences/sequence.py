from math import sqrt


def sequence(rule, *args, **kwargs):
    return lambda n: [rule(x+1) for x in range(n)]


def clean_up(lst):
    return list(map(float, (map('{:.2f}'.format, lst))))


def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def fib(n):
    p = 1.618034
    return int((p ** n - (1 - p) ** n) // sqrt(5))


def harmonic(n):
    return 1 / n


def alt_harmonic(n):
    return (-1) ** (n + 1) / n


def powers(x):
    return lambda n: x ** n


def multiples(x):
    return lambda n: x * n


if __name__ == '__main__':
    print("tests")

    print(triangle(6))

    print(square(6))

    print(cube(6))

    print(sequence(fib)(6))

    print(clean_up(sequence(harmonic)(6)))

    print('log 2 =', sum(sequence(alt_harmonic)(100)))

    eights = powers(8)

    print(sequence(eights)(6))

    threes = multiples(3)

    print(sequence(threes)(6))

    sevens = multiples(8)

    print(sequence(sevens)(10))


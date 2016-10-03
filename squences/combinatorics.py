from math import factorial


def fact(n):
    product = 1
    for i in reversed(range(n)):
        product *= (i + 1)
    return product


# x items into y buckets  things (order matters)
def permutations(n, m):
    return factorial(n) / factorial(n - m)


# combinations (don't care about order), select x out y things
def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    print('Tests')

    assert fact(23) == factorial(23), '23!'

    assert permutations(10, 4) == 5040, '10P4'

    assert combinations(10, 5) == 252, '10C5'

    result = permutations(3, 2)
    print(result)

    result = combinations(4, 2)
    print(result)

    print(factorial(4))
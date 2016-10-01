# triangle numbers: +1...
def triangle_sequence(n, start=1):
    total = 0
    for i in range(n):
        total += start + i
    return total


# n = height also width of last row
def tri_seq(n):
    return n * (n+1) // 2


# square numbers: +1, +3, +5, +7, ...
def square_sequence(n, start=1):
    total = 0
    for i in range(n):
        total += start + i + 2
    return total


def fibonacci(n):
    if n < 3:
        return 1
    f = [1, 1]
    for i in range(n - 2):
        temp = f[1]
        f[1] += f[0]
        f[0] = temp
    return f[1]

if __name__ == '__main__':
    print(triangle_sequence(5))
    assert triangle_sequence(5) == 15, 'n=5'

    print(tri_seq(5))
    assert tri_seq(5) == 15, 'n=5'

    print(square_sequence(5))
    assert square_sequence(5) == 25, 'n=5'

    print(fibonacci(6))
    assert fibonacci(6) == 8, 'n=6'


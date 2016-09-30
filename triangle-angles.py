from math import acos, degrees


def checkio(a, b, c):
    def law_of_cosine(a, b, c):
        return round(degrees(acos((a * a + b * b - c * c) / (2 * a * b))))

    try:
        A = law_of_cosine(b, c, a)
        B = law_of_cosine(a, c, b)
        C = law_of_cosine(a, b, c)

        if A == 0 or B == 0 or C == 0:
            raise ValueError()

        return sorted([A, B, C])

    except ValueError:
        return [0, 0, 0]



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

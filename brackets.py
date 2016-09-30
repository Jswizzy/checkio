def checkio(expression):
    lookup = {')': '(', '}': '{', ']': '['}

    stack = []

    for ch in expression:

        if ch in lookup.values():
            stack.append(ch)

        elif ch in lookup.keys():
            if not len(stack) or stack.pop() != lookup[ch]:
                return False

    return len(stack) == 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(((1+(1+1))))]") == False, "Fail"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

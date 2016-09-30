def checkio(time_string):
    time_array = time_string.split(':')

    binary = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True)

    result = []
    for string in time_array:
        time = []
        if len(string) == 1:
            string = '0' + string
        for ch in string:
            i = int(ch)
            digit = ''
            for b in binary:
                if i >= b:
                    digit += '-'
                    i -= b
                else:
                    digit += '.'
            time.append(digit[3:])
        result.append(time)

    # print(result)
    #
    # print("{0} {1} : {2} {3} : {4} {5}".format((result[0][0][-2:]), result[0][1],
    #               (result[1][0][-3:]), result[1][1],
    #               (result[2][0][-3:]), result[2][1]))

    return "{0} {1} : {2} {3} : {4} {5}".format((result[0][0][-2:]), result[0][1],
                  (result[1][0][-3:]), result[1][1],
                  (result[2][0][-3:]), result[2][1])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

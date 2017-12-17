#!/usr/bin/env pypy


def solve(problem):
    n = int(problem)

    a = [0]
    pos = 0

    for x in range(1, 2018):
        pos = (pos + n) % len(a) + 1
        a.insert(pos, x)

    res = a[(pos + 1) % len(a)]
    return res


def test():
    assert solve('3') == 638


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

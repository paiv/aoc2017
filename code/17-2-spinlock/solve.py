#!/usr/bin/env pypy
from __future__ import print_function


def solve(problem):
    n = int(problem)

    pos = 0
    res = 0

    for x in range(1, 50000001):
        pos = (pos + n) % x + 1
        if pos == 1:
            res = x

    return res


def test():
    pass


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env python3


def solve(t):
    n = len(t) // 2
    return sum((int(a) * (a == b)) for a,b in zip(t, t[n:] + t[:n]))


def test():
    assert solve('1212') == 6
    assert solve('1221') == 0
    assert solve('123425') == 4
    assert solve('123123') == 12
    assert solve('12131415') == 4


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

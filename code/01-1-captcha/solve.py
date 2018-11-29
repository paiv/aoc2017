#!/usr/bin/env python3


def solve(t):
    return sum((int(a) * (a == b)) for a,b in zip(t, t[1:] + t[:1]))


def test():
    assert solve('1111') == 4
    assert solve('1122') == 3
    assert solve('1234') == 0
    assert solve('91212129') == 9


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

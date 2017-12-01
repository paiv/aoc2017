#!/usr/bin/env python3


def solve(t):
    n = len(t)

    res = sum(int(t[i]) if t[i] == t[(i + n // 2) % n] else 0 for i in range(0, len(t)))
    # print(res)
    return res


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

#!/usr/bin/env python3


def solve(t):
    n = len(t)

    res = sum(int(t[i]) if t[i] == t[(i + 1) % n] else 0 for i in range(0, len(t)))
    # print(res)
    return res


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

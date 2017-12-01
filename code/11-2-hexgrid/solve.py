#!/usr/bin/env python3


def solve(problem):
    r = 0
    q = 0

    res = 0

    for m in problem.split(','):
        if m == 'ne':
            q += 1
            r += -1
        elif m == 'n':
            q += 0
            r += -1
        elif m == 'nw':
            q += -1
            r += 0
        elif m == 'sw':
            q += -1
            r += 1
        elif m == 's':
            q += 0
            r += 1
        elif m == 'se':
            q += 1
            r += 0

        res = max(res, max(abs(r), abs(q), abs(-r-q)))

    return res


def test():
    assert solve('ne,ne,ne') == 3
    assert solve('ne,ne,s,sw,nw') == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

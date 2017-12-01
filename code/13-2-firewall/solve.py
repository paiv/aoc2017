#!/usr/bin/env python3
import itertools


def solve(problem):
    d = dict(map(int, line.split(': ')) for line in problem.splitlines())

    def xx(i, x):
        y = (x - 1) * 2
        z = i % y
        if z >= x:
            z = y - z
        if z == 0:
            return i * x
        return 0

    def sev(t):
        return any(xx(i + t, d[i]) for i in d)

    for delay in itertools.count():
        if not sev(delay):
            return delay

    return res


def test():
    problem = """
0: 3
1: 2
4: 4
6: 4
""".strip()

    assert solve(problem) == 10


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

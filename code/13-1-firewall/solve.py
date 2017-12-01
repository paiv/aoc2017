#!/usr/bin/env python3


def solve(problem):
    d = dict(map(int, line.split(': ')) for line in problem.splitlines())

    res = 0
    for i in d:
        x = d[i]
        y = (x - 1) * 2
        z = i % y
        if z >= x:
            z = y - z

        if z == 0:
            res += i * x

    return res


def test():
    problem = """
0: 3
1: 2
4: 4
6: 4
""".strip()

    assert solve(problem) == 24


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

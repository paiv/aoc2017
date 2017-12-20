#!/usr/bin/env pypy
from __future__ import print_function


def solve(problem):
    ps = [line.strip().split(', ') for line in problem.splitlines()]
    ps = [tuple(p.split('=') for p in line) for line in ps]
    ps = [{p[0]: list(map(int, p[1][1:-1].split(','))) for p in line} for line in ps]
    ps = [[p['a'], p['v'], p['p']] for p in ps]

    for _ in range(10000):
        for p in ps:
            for i in range(3):
                p[1][i] += p[0][i]
                p[2][i] += p[1][i]

    ps = [sum(map(abs, p[2])) for p in ps]
    res = ps.index(min(ps))

    return res


def test():
    problem = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".strip('\n')

    assert solve(problem) == 0


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

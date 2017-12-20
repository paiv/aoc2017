#!/usr/bin/env pypy
from __future__ import print_function


def solve(problem):
    ps = [line.strip().split(', ') for line in problem.splitlines()]
    ps = [tuple(p.split('=') for p in line) for line in ps]
    ps = [{p[0]: list(map(int, p[1][1:-1].split(','))) for p in line} for line in ps]
    ps = [[p['a'], p['v'], p['p']] for p in ps]

    for kk in range(1000):
        for p in ps:
            for i in range(3):
                p[1][i] += p[0][i]
                p[2][i] += p[1][i]

        excl = set()
        for i in range(len(ps) - 1):
            for j in range(i + 1, len(ps)):
                if ps[i][2] == ps[j][2]:
                    excl.add(i)
                    excl.add(j)
        ps = [p for i,p in enumerate(ps) if i not in excl]

    return len(ps)


def test():
    problem = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
""".strip('\n')

    assert solve(problem) == 1


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

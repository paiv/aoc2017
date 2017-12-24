#!/usr/bin/env pypy3
from collections import defaultdict


def solve(problem):
    parts = [tuple(map(int, line.split('/'))) for line in problem.splitlines()]

    byport = defaultdict(set)
    for p,q in parts:
        byport[p].add(q)
        byport[q].add(p)

    def gen(p,acc,visited):
        for q in byport[p]:
            vv = tuple(sorted((p,q)))
            if vv not in visited:
                xm = acc + p + q
                xv = visited | set([vv])
                yield xm
                # yield from gen(q, xm, xv)  # slow in pypy3
                for zz in gen(q, xm, xv):
                    yield zz

    res = 0
    for m in gen(0, 0, set()):
        res = max(res, m)

    return res


def test():
    problem = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip('\n')

    assert solve(problem) == 31


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

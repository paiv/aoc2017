#!/usr/bin/env pypy3
from __future__ import division, print_function
from collections import defaultdict


def solve(problem, n=10000):
    a = [[c != '.' for c in line] for line in problem.splitlines()]
    w = len(a)
    h = w // 2

    moves = [
        1+0j, # right
        0-1j, # up
        -1+0j, # left
        0+1j, # down
    ]

    sz = n
    grid = defaultdict(int)
    pos = complex(sz,sz)
    d = 1 # right, up, left, down

    for r in range(w):
        for c in range(w):
            if a[r][c]:
                grid[(sz-h+r, sz-h+c)] = 1

    res = 0

    for _ in range(n):
        pp = (int(pos.imag), int(pos.real))
        q = grid[pp]

        x = -1 if q else 1
        d = (d + x) % 4

        # clean, infected
        q = 1 - q

        grid[pp] = q
        pos += moves[d]

        res += q

    return res


def test():
    problem = """
..#
#..
...
""".strip('\n')

    assert solve(problem, 7) == 5
    assert solve(problem, 70) == 41
    assert solve(problem, 10000) == 5587


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

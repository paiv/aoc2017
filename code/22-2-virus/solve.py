#!/usr/bin/env pypy3
from __future__ import division, print_function
from collections import defaultdict


def solve(problem, n=10000000):
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
                grid[(sz-h+r, sz-h+c)] = 2

    res = 0

    for _ in range(n):
        pp = (int(pos.imag), int(pos.real))
        q = grid[pp]

        x = 0
        if q == 0:
            x = 1
        elif q == 2:
            x = -1
        elif q == 3:
            x = 2

        d = (d + x) % 4

        # clean, weak, infected, flagged
        q = (q + 1) % 4

        grid[pp] = q
        pos += moves[d]

        if q == 2:
            res += 1

        # print(pos, q)
        # print('\n'.join(''.join(map('{:2}'.format, (grid[(r,c)] for c in range(sz*2)))) for r in range(sz*2)))

    return res


def test():
    problem = """
..#
#..
...
""".strip('\n')

    assert solve(problem, 7) == 1
    assert solve(problem, 100) == 26


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

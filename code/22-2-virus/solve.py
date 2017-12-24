#!/usr/bin/env pypy3
from collections import defaultdict
from functools import reduce


def dump(grid):
    print()
    minx = reduce(min, (k.real for k in grid.keys()))
    maxx = reduce(max, (k.real for k in grid.keys()))
    miny = reduce(min, (k.imag for k in grid.keys()))
    maxy = reduce(max, (k.imag for k in grid.keys()))

    s = '\n'.join(''.join(map('{:3}'.format, (grid[c+r*1j] for c in range(int(minx), int(maxx) + 1))))
        for r in range(int(miny), int(maxy) + 1))
    print(s)


def solve(problem, n=10000000):
    a = [[c != '.' for c in line] for line in problem.splitlines()]
    w = len(a)
    h = w // 2

    moves = (
        1,   # right
        -1j, # up
        -1,  # left
        1j,  # down
    )

    turns = (
        1,  # clean, turn left
        0,  # weak, continue
        -1, # infected, turn right
        2,  # flagged, reverse
    )

    grid = defaultdict(int)
    pos = 0j
    d = 1 # right, up, left, down

    for r in range(w):
        for c in range(w):
            grid[complex(-h+c, -h+r)] = 2 if a[r][c] else 0

    res = 0

    for _ in range(n):
        q = grid[pos]

        d = (d + turns[q]) % 4

        # clean, weak, infected, flagged
        q = (q + 1) % 4

        grid[pos] = q
        pos += moves[d]

        if q == 2:
            res += 1

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

#!/usr/bin/env python
import numpy as np


def parse(s):
    a = [[c != '.' for c in r] for r in s.split('/')]
    return np.array(a)


def unparse(a):
    return '/'.join(''.join('#' if c else '.' for c in r) for r in a)


def solve(problem, steps=18):
    grid = parse(".#./..#/###")

    book = dict()

    for line in problem.splitlines():
        a,b = line.strip().split(' => ')
        m = parse(a)
        for _ in range(4):
            book[unparse(m)] = b
            book[unparse(np.flipud(m))] = b
            book[unparse(np.fliplr(m))] = b
            m = np.rot90(m)


    def roll(a, sa):
        wa = a.shape[1] // sa
        sb = sa + 1
        wb = wa * sb
        b = np.zeros((wb,wb), dtype=np.bool)
        for r in range(wa):
            for c in range(wa):
                x = a[r*sa:(r+1)*sa, c*sa:(c+1)*sa]
                x = unparse(x)
                y = parse(book[x])
                b[r*sb:(r+1)*sb, c*sb:(c+1)*sb] = y
        return b


    for _ in range(steps):
        stride = 2 + grid.shape[0] % 2
        grid = roll(grid, stride)

    res = np.sum(grid)

    return res


def test():
    assert np.all(parse('#.#/.#.') == np.array([[True, False, True], [False, True, False]]))
    assert unparse(parse('#.#/.#.')) == '#.#/.#.'

    problem = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip('\n')

    assert solve(problem, 2) == 12


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env python3
import itertools
import math


def solve(problem):

    def check(xs):
        x,y = next((x,y) for x, y in itertools.combinations(xs, 2) if math.gcd(x,y) > 1)
        return x // y or y // x

    spreadsheet = [[int(x) for x in line.split()] for line in problem.splitlines()]
    return sum(check(row) for row in spreadsheet)


def test():

    problem = """
5 9 2 8
9 4 7 3
3 8 6 5
""".strip()

    assert solve(problem) == 9


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

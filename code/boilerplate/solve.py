#!/usr/bin/env pypy
from __future__ import print_function
#              python3
# import numpy as np
# import re
# from collections import defaultdict


def solve(problem):
    # a: 12345
    # n = int(problem)

    # a: 1 2 3 4 5
    # a = [int(x) for x in problem.split()]

    # a: 1 2 3
    #    4 5 6
    # a = [list(map(int, l.split())) for l in problem.splitlines()]

    # rx = re.compile(r'^(.*?)$', re.M)
    # a = rx.findall(problem)
    # assert len(a) == len(problem.splitlines())

    # a: xy op -4 zz rq ...
    # a = [l.split() for l in problem.splitlines()]


    res = 0
    print(res)
    return res


def test():
    problem = """
""".strip()

    # assert solve(problem) == 0

    # assert solve('') == 0


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

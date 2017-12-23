#!/usr/bin/env pypy3
# from collections import defaultdict


def solve(problem):

    res = 0
    print(res)
    return res


def test():
    problem = """
""".strip('\n')

    # assert solve(problem) == 0

    # assert solve('') == 0


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

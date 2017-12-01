#!/usr/bin/env python3
from collections import defaultdict


def solve(problem):
    prog = [l.split() for l in problem.splitlines()]

    state = defaultdict(int)
    res = 0

    for r,op,x,_,c,cond,v in prog:
        c = state[c]
        x = int(x)
        v = int(v)

        t = False

        if cond == '>':
            t = c > v
        elif cond == '>=':
            t = c >= v
        elif cond == '<':
            t = c < v
        elif cond == '<=':
            t = c <= v
        elif cond == '==':
            t = c == v
        elif cond == '!=':
            t = c != v

        if t:
            if op == 'inc':
                state[r] = state[r] + x
            elif op == 'dec':
                state[r] = state[r] - x

            res = max(res, max(state.values()))

    # print(res)
    return res


def test():
    problem = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip()

    assert solve(problem) == 10


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

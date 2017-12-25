#!/usr/bin/env pypy3
from collections import defaultdict


def parse(lines):
    def pp(ll):
        w = int(ll[0][-2])
        m = 1 if ll[1][:-1].split()[-1] == 'right' else -1
        n = ll[2][-2]
        return (w,m,n)

    state = lines[0][-2]
    case0 = pp(lines[2:5])
    case1 = pp(lines[6:9])
    return (state, case0, case1)


def solve(problem):
    lines = problem.splitlines()
    n = int(lines[1].split()[5])

    prog = dict()

    for i in range(3, len(lines), 10):
        st = parse(lines[i:i+10])
        prog[st[0]] = st[1:]

    pos = 0
    state = 'A'
    tape = defaultdict(int)

    for _ in range(n):
        x = tape[pos]
        p = prog[state][x]
        tape[pos] = p[0]
        pos += p[1]
        state = p[2]

    res = sum(tape.values())
    return res


def test():
    problem = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
""".strip('\n')

    assert solve(problem) == 3


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env pypy
from __future__ import print_function
from collections import defaultdict


def parse(text):
    prog = []

    def arg(x):
        if x.isalpha():
            return x
        return int(x)


    for line in text.strip().splitlines():
        cmd = line.split()
        op = cmd[0]
        a = arg(cmd[1])
        b = arg(cmd[2]) if len(cmd) == 3 else None

        prog.append((op, a, b))

    return prog


def solve(problem):
    prog = parse(problem)

    regs = defaultdict(int)
    ip = 0
    snd = 0

    def arg(x):
        if isinstance(x, str):
            return regs[x]
        return x


    while ip >= 0 and ip < len(prog):

        op,a,b = prog[ip]

        if op == 'set':
            regs[a] = arg(b)
        elif op == 'add':
            regs[a] += arg(b)
        elif op == 'mul':
            regs[a] *= arg(b)
        elif op == 'mod':
            regs[a] %= arg(b)
        elif op == 'jgz':
            if arg(a) > 0:
                ip += arg(b) - 1
        elif op == 'snd':
            snd = arg(a)
        elif op == 'rcv':
            if arg(a) != 0:
                regs[a] = snd
                break

        ip += 1


    res = snd
    return res


def test():
    problem = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
""".strip()

    assert solve(problem) == 4


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env pypy3
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
        a = arg(cmd[1]) if len(cmd) > 1 else None
        b = arg(cmd[-1]) if len(cmd) > 2 else None

        prog.append((op, a, b))

    return prog


def solve(problem):
    prog = parse(problem)

    regs = defaultdict(int)

    def arg(x):
        if isinstance(x, str):
            return regs[x]
        return x

    res = 0

    ip = 0
    while ip >= 0 and ip < len(prog):
        op,a,b = prog[ip]

        saved_ip = ip

        if op == 'set':
            regs[a] = arg(b)
        elif op == 'sub':
            regs[a] -= arg(b)
        elif op == 'mul':
            regs[a] *= arg(b)
            res += 1
        elif op == 'jnz':
            if arg(a) != 0:
                ip += arg(b) - 1
        else:
            raise Exception('unhandled op at {} {}'.format(ip, prog[ip]))

        ip += 1

    return res


def test():
    pass


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

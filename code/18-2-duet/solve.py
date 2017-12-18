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
        b = arg(cmd[-1]) if len(cmd) == 3 else None

        prog.append((op, a, b))

    return prog


def solve(problem):
    prog = parse(problem)

    regs = [defaultdict(int) for _ in range(2)]
    done = [False] * 2
    waiting = [False] * 2
    msg = [list() for _ in range(2)]

    regs[1]['p'] = 1
    res = 0

    def arg(pid, x):
        if isinstance(x, str):
            return regs[pid][x]
        return x


    while not all(done):
        if all(waiting):
            break

        for p in range(2):

            ip = regs[p]['ip']

            if ip < 0 or ip >= len(prog):
                done[p] = True
            else:
                op,a,b = prog[ip]

                saved_ip = ip

                if op == 'set':
                    regs[p][a] = arg(p, b)
                elif op == 'add':
                    regs[p][a] += arg(p, b)
                elif op == 'mul':
                    regs[p][a] *= arg(p, b)
                elif op == 'mod':
                    regs[p][a] %= arg(p, b)
                elif op == 'jgz':
                    if arg(p, a) > 0:
                        ip += arg(p, b) - 1

                elif op == 'snd':
                    msg[1-p].append(arg(p, a))

                    if p == 1:
                        res += 1

                elif op == 'rcv':
                    if len(msg[p]):
                        waiting[p] = False
                        regs[p][a] = msg[p].pop(0)
                    else:
                        waiting[p] = True
                        continue

                ip += 1
                regs[p]['ip'] = ip

    return res


def test():
    problem = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
""".strip()

    assert solve(problem) == 3

    problem = """
jgz p 2
snd 1
snd 2
jgz 3 2
snd p
""".strip()

    assert solve(problem) == 1


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

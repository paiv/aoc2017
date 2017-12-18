#!/usr/bin/env pypy
from __future__ import print_function
import multiprocessing as mp
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


def prog_run(pid, prog, sendq, recvq):
    regs = defaultdict(int)
    regs['p'] = pid

    def arg(x):
        if isinstance(x, str):
            return regs[x]
        return x

    ip = 0
    snd_count = 0

    while ip >= 0 and ip < len(prog):

        op,a,b = prog[ip]
        saved_ip = ip

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
            sendq.put(arg(a))
            snd_count += 1

        elif op == 'rcv':
            try:
                regs[a] = recvq.get(timeout=0.1)
            except:
                return snd_count

        ip += 1

    return snd_count


def solve(problem):
    prog = parse(problem)

    a2b = mp.Queue()
    b2a = mp.Queue()

    p0 = mp.Process(target=prog_run, args=(0, prog, a2b, b2a))
    p0.start()

    res = prog_run(1, prog, b2a, a2b)

    p0.join()

    return res


def test():
    problem = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
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

#!/usr/bin/env pypy3
# Generated with Duet https://github.com/paiv/aoc2017


class DuetVM:
    IP, SND = 0, 1


def addi(x, y, regs):
    regs[x] += y
def addr(x, y, regs):
    regs[x] += regs[y]
def jgii(x, y, regs):
    if x > 0:
        regs[DuetVM.IP] += y - 1
def jgrr(x, y, regs):
    if regs[x] > 0:
        regs[DuetVM.IP] += regs[y] - 1
def jgri(x, y, regs):
    if regs[x] > 0:
        regs[DuetVM.IP] += y - 1
def modi(x, y, regs):
    regs[x] %= y
def modr(x, y, regs):
    regs[x] %= regs[y]
def muli(x, y, regs):
    regs[x] *= y
def rcv(x, y, regs):
    if regs[x]:
        regs[x] = regs[DuetVM.SND]
        # part1:
        regs[DuetVM.IP] = float('inf')
def seti(x, y, regs):
    regs[x] = y
def setr(x, y, regs):
    regs[x] = regs[y]
def sndr(x, y, regs):
    regs[DuetVM.SND] = regs[x]


instr = (addi, addr, jgii, jgri, jgrr, modi, modr, muli, rcv, seti, setr, sndr)


program = (
    (9, 5, 31),
    (9, 2, 1),
    (7, 6, 17),
    (4, 6, 6),
    (7, 2, 2),
    (0, 5, -1),
    (3, 5, -2),
    (0, 2, -1),
    (9, 5, 127),
    (9, 6, 622),
    (7, 6, 8505),
    (6, 6, 2),
    (7, 6, 129749),
    (0, 6, 12345),
    (6, 6, 2),
    (10, 3, 6),
    (5, 3, 10000),
    (11, 3, 0),
    (0, 5, -1),
    (3, 5, -9),
    (3, 2, 3),
    (8, 3, 0),
    (3, 3, -1),
    (9, 4, 0),
    (9, 5, 126),
    (8, 2, 0),
    (8, 3, 0),
    (10, 6, 2),
    (7, 6, -1),
    (1, 6, 3),
    (3, 6, 4),
    (11, 2, 0),
    (10, 2, 3),
    (2, 1, 3),
    (11, 3, 0),
    (9, 4, 1),
    (0, 5, -1),
    (3, 5, -11),
    (11, 2, 0),
    (3, 4, -16),
    (3, 2, -19),
    )


def main():
    #    ip, snd, a, b, f, i, p, 
    regs = [0, 0, 0, 0, 0, 0, 0]
    ip = 0

    while 0 <= ip < len(program):
        regs[DuetVM.IP] = ip
        op, x, y = program[ip]
        instr[op](x, y, regs)
        ip = regs[DuetVM.IP] + 1

    return regs[DuetVM.SND]


if __name__ == '__main__':
    print(main())

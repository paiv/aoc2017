from collections import defaultdict


class Image:
    def __init__(self, program, regs=None, ip=0, register_names=None):
        self.program = program
        self.regs = regs
        self.register_names = register_names
        if self.register_names:
            assert self.register_names[0] == 'ip'
        if not self.regs and self.register_names:
            self.regs = [0 for _ in self.register_names]
        self.regs[0] = ip

    @property
    def ip(self):
        return self.regs[0]


class DuetVM:

    IP, SND = 0, 1

    def addi(x, y, regs):
        regs[x] += y
    def addr(x, y, regs):
        regs[x] += regs[y]
    def jgii(x, y, regs):
        if x > 0:
            regs[DuetVM.IP] += y - 1
    def jgir(x, y, regs):
        if x > 0:
            regs[DuetVM.IP] += regs[y] - 1
    def jgri(x, y, regs):
        if regs[x] > 0:
            regs[DuetVM.IP] += y - 1
    def jgrr(x, y, regs):
        if regs[x] > 0:
            regs[DuetVM.IP] += regs[y] - 1
    def modi(x, y, regs):
        regs[x] %= y
    def modr(x, y, regs):
        regs[x] %= regs[y]
    def muli(x, y, regs):
        regs[x] *= y
    def mulr(x, y, regs):
        regs[x] *= regs[y]
    def rcv(x, y, regs):
        if regs[x]:
            regs[x] = regs[DuetVM.SND]
    def seti(x, y, regs):
        regs[x] = y
    def setr(x, y, regs):
        regs[x] = regs[y]
    def sndi(x, y, regs):
        regs[DuetVM.SND] = x
    def sndr(x, y, regs):
        regs[DuetVM.SND] = regs[x]
    def subi(x, y, regs):
        regs[x] -= y
    def subr(x, y, regs):
        regs[x] -= regs[y]

    instr = dict(
        addi=addi, addr=addr,
        jgii=jgii, jgir=jgir, jgrr=jgrr, jgri=jgri,
        modi=modi, modr=modr,
        muli=muli, mulr=mulr,
        rcv=rcv, sndi=sndi, sndr=sndr,
        seti=seti, setr=setr,
    )

    INSTRUCTIONS = frozenset(instr.keys())

    def __init__(self, image):
        self.image = image

    def run(self, query=None):
        program = self.image.program
        regs = list(self.image.regs)
        rnames = self.image.register_names
        ip = self.image.ip
        instr = self.instr

        while 0 <= ip < len(program):
            regs[0] = ip
            op, x, y = program[ip]
            instr[op](x, y, regs=regs)
            ip = regs[0] + 1

        self.image = Image(program, regs=regs, ip=ip, register_names=rnames)

        if query:
            return regs[rnames.index(query)]

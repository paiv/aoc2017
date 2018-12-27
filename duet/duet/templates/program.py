#!/usr/bin/env pypy3
# Generated with Duet https://github.com/paiv/aoc2017


class DuetVM:
    IP, SND = 0, 1

{% if 'addi' in instructions %}
def addi(x, y, regs):
    regs[x] += y
{%- endif %}

{%- if 'addr' in instructions %}
def addr(x, y, regs):
    regs[x] += regs[y]
{%- endif %}

{%- if 'jgii' in instructions %}
def jgii(x, y, regs):
    if x > 0:
        regs[DuetVM.IP] += y - 1
{%- endif %}

{%- if 'jgir' in instructions %}
def jgir(x, y, regs):
    if x > 0:
        regs[DuetVM.IP] += regs[y] - 1
{%- endif %}

{%- if 'jgrr' in instructions %}
def jgrr(x, y, regs):
    if regs[x] > 0:
        regs[DuetVM.IP] += regs[y] - 1
{%- endif %}

{%- if 'jgri' in instructions %}
def jgri(x, y, regs):
    if regs[x] > 0:
        regs[DuetVM.IP] += y - 1
{%- endif %}

{%- if 'modi' in instructions %}
def modi(x, y, regs):
    regs[x] %= y
{%- endif %}

{%- if 'modr' in instructions %}
def modr(x, y, regs):
    regs[x] %= regs[y]
{%- endif %}

{%- if 'muli' in instructions %}
def muli(x, y, regs):
    regs[x] *= y
{%- endif %}

{%- if 'mulr' in instructions %}
def mulr(x, y, regs):
    regs[x] *= regs[y]
{%- endif %}

{%- if 'rcv' in instructions %}
def rcv(x, y, regs):
    if regs[x]:
        regs[x] = regs[DuetVM.SND]
{%- endif %}

{%- if 'seti' in instructions %}
def seti(x, y, regs):
    regs[x] = y
{%- endif %}

{%- if 'setr' in instructions %}
def setr(x, y, regs):
    regs[x] = regs[y]
{%- endif %}

{%- if 'sndi' in instructions %}
def sndi(x, y, regs):
    regs[DuetVM.SND] = x
{%- endif %}

{%- if 'sndr' in instructions %}
def sndr(x, y, regs):
    regs[DuetVM.SND] = regs[x]
{%- endif %}


instr = ({% for name in instructions %}{{name}}{% if not loop.last %}, {% endif %}{% endfor %})


program = (
    {%- for line in program %}
    {{line}},
    {%- endfor %}
    )


def main():
    #    {% for name in register_names %}{{name}}, {% endfor %}
    regs = {{registers}}
    ip = {{ip}}

    while 0 <= ip < len(program):
        regs[DuetVM.IP] = ip
        op, x, y = program[ip]
        instr[op](x, y, regs)
        ip = regs[DuetVM.IP] + 1

    return regs[DuetVM.SND]


if __name__ == '__main__':
    print(main())

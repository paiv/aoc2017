#!/usr/bin/env python3
import itertools
import re


instr_rx = re.compile(r'\s*(add|cpy|inc|dec|jnz|mul|nop|out)\s*(?:([a-d])|(\-?\d+))?\s*(?:([a-d])|(\-?\d+))?')

def parse_instr(text):
    m = instr_rx.match(text)

    instr = m.group(1)
    x = None
    y = None

    if m.group(2):
        x = m.group(2)
    elif m.group(3):
        x = int(m.group(3))

    if m.group(4):
        y = m.group(4)
    elif m.group(5):
        y = int(m.group(5))

    return (instr, x, y)


def make_state(a=0, b=0, c=0, d=0):
    return {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    }


def dump_state(prog, ip, state):
    prog = '\n'.join('{:2}:  {}'.format(i, ' '.join(str(x) for x in p)) for i,p in enumerate(prog))
    state = ' '.join('{}:{}'.format(k, v) for k,v in state.items())
    return 'ip:{} {}\n{}'.format(ip, state, prog)


def vm(prog, state):
    ip = 0
    last_state = (ip, state['a'], state['b'], state['c'], state['d'])
    prog = list(prog)
    instr_count = 0

    # print('-- ', instr_count)
    # print(dump_state(prog, ip, state))

    while ip >= 0 and ip < len(prog):
        instr,x,y = prog[ip]

        instr_count += 1

        if instr == 'nop':
            pass

        elif instr == 'cpy':
            if isinstance(x, str):
                x = state[x]
            state[y] = x

        elif instr == 'inc':
            v = state[x]
            v += 1
            state[x] = v

        elif instr == 'dec':
            v = state[x]
            v -= 1
            state[x] = v

        elif instr == 'jnz':
            if isinstance(x, str):
                x = state[x]
            if x != 0:
                if isinstance(y, str):
                    y = state[y]
                ip += y - 1

        elif instr == 'mul':
            if isinstance(x, str):
                x = state[x]
            state['a'] *= x

        elif instr == 'add':
            if isinstance(x, str):
                x = state[x]
            state['a'] += x

        elif instr == 'out':
            if isinstance(x, str):
                x = state[x]
            yield x

        else:
            raise Exception('invalid instruction {}: {}'.format(ip, prog[ip]))

        ip += 1


        current_state = (ip, state['a'], state['b'], state['c'], state['d'])
        if current_state == last_state:
            print('! killed')
            break
        else:
            last_state = current_state

    # return state


def solve(problem):
    prog = [parse_instr(s) for s in problem.splitlines()]

    state = make_state()
    res = ''.join(chr(x) for x in vm(prog, state))
    return res


def test():
    pass


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

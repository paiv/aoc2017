#!/usr/bin/env python3
import string


def solve(problem, n=16):
    cs = problem.split(',')
    progs = list(string.ascii_lowercase[:n])

    def parse(c):
        if c[0] == 's':
            x = int(c[1:])
            return (0, x, None)
        elif c[0] == 'x':
            a,b = tuple(map(int, c[1:].split('/')))
            return (1, a, b)
        elif c[0] == 'p':
            a,b = tuple(c[1:].split('/'))
            return (2, a, b)

    cs = [parse(x) for x in cs]

    p = list(progs)
    res = []

    for c,a,b in cs:
        if c == 0:
            p = p[-a:] + p[:-a]

        elif c == 1:
            p[a],p[b] = p[b],p[a]

        elif c == 2:
            x,y = p.index(a), p.index(b)
            p[x],p[y] = p[y],p[x]


    res = ''.join(p)
    return res


def test():
    assert solve('s1,x3/4,pe/b', n=5) == 'baedc'


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env python3
import operator
from functools import reduce


def knothash(text):
    a = [ord(x) for x in text] + [17, 31, 73, 47, 23]

    def roundrun(b, a, pos, skip):
        for x in a:

            x = a[skip % len(a)]
            y = min(len(b), pos + x)
            z = max(0, (pos + x) - len(b))

            p = b[pos: y]
            q = b[: z]

            s = p + q
            s = list(reversed(s))

            b[pos: y] = s[:len(p)]
            b[: z] = s[len(p):]

            pos = (pos + x + skip) % len(b)
            skip += 1

        return (b, pos, skip)


    b = list(range(256))
    pos = 0
    skip = 0

    for i in range(64):
        b, pos, skip = roundrun(b, a, pos, skip)

    z = [b[x:x+16] for x in range(0, len(b), 16)]
    z = [reduce(operator.xor, x) for x in z]
    # res = ''.join('{:02x}'.format(x) for x in z)
    return z


def solve(problem):

    disk = []
    for i in range(128):
        row = knothash('{}-{}'.format(problem, i))
        disk.append(''.join('{:08b}'.format(x) for x in row))

    res = 0

    visit = set((x,y) for y in range(128) for x in range(128) if disk[y][x] != '0')

    while visit:
        res += 1
        fringe = [visit.pop()]
        visit.add(fringe[0])

        while fringe:
            p = fringe.pop(0)
            if p in visit:
                visit.remove(p)

                x,y = p
                for q in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    fringe.append(q)
    return res


def test():
    assert solve('flqrgnkx') == 1242


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

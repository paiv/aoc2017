#!/usr/bin/env python3
import operator
from functools import reduce


def solve(problem, n=256):
    a = [ord(x) for x in problem] + [17, 31, 73, 47, 23]

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


    b = list(range(n))
    pos = 0
    skip = 0

    for i in range(64):
        b, pos, skip = roundrun(b, a, pos, skip)

    z = [b[x:x+16] for x in range(0, len(b), 16)]
    z = [reduce(operator.xor, x) for x in z]
    res = ''.join('{:02x}'.format(x) for x in z)

    return res


def test():
    assert solve('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert solve('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert solve('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert solve('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

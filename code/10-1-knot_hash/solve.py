#!/usr/bin/env python3


def solve(problem, n=256):
    a = [int(x.strip()) for x in problem.split(',')]

    b = list(range(n))

    pos = 0
    for skip in range(len(a)):

        x = a[skip]
        y = min(len(b), pos + x)
        z = max(0, (pos + x) - len(b))

        p = b[pos: y]
        q = b[: z]

        s = p + q
        s = list(reversed(s))

        b[pos: y] = s[:len(p)]
        b[: z] = s[len(p):]

        pos = (pos + x + skip) % len(b)

    res = b[0] * b[1]
    return res


def test():
    assert solve('3, 4, 1, 5', n=5) == 12


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

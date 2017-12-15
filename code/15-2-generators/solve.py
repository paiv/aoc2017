#!/usr/bin/env pypy


def solve(problem):
    a, b = tuple(int(line.strip().split()[4]) for line in problem.splitlines())

    ax = 16807
    bx = 48271

    m = 2147483647 # 0x7fffffff
    n = 5 * 1000000

    def xs(v, x, m, q):
        while True:
            v = v * x % m
            if v % q == 0:
                yield v & 0xffff

    res = sum(x == y for x,y,i in zip(xs(a, ax, m, 4), xs(b, bx, m, 8), range(n)))

    return res


def test():
    problem = """
Generator A starts with 65
Generator B starts with 8921
""".strip()

    assert solve(problem) == 309


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

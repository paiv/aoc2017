#!/usr/bin/env pypy


def solve(problem):
    a, b = tuple(int(line.strip().split()[4]) for line in problem.splitlines())

    ax = 16807
    bx = 48271

    m = 2147483647 # 0x7fffffff
    n = 40 * 1000000

    def xs(v, x, m):
        while True:
            v = v * x % m
            yield v & 0xffff

    res = sum(x == y for x,y,i in zip(xs(a, ax, m), xs(b, bx, m), range(n)))

    return res


def test():
    problem = """
Generator A starts with 65
Generator B starts with 8921
""".strip()

    assert solve(problem) == 588


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip()
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

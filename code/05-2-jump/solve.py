#!/usr/bin/env python3


def solve(problem):
    prog = [int(x) for line in problem.splitlines() for x in line.split()]

    ip = 0
    steps = 0
    while True:
        x = prog[ip]
        prog[ip] += 1 if x < 3 else -1
        ip += x
        steps += 1

        if ip < 0 or ip >= len(prog):
            break

    # print(steps)
    return steps


def test():
    problem = """
0
3
0
1
-3
""".strip()

    assert solve(problem) == 10


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

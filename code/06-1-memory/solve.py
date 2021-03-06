#!/usr/bin/env python3


def solve(problem):
    problem = [int(x) for x in problem.split()]

    state = tuple(problem)

    visited = set()
    res = 0

    while True:
        if state in visited:
            break

        visited.add(state)
        res += 1

        a = list(state)
        i = a.index(max(a))
        x = a[i]
        a[i] = 0
        while x > 0:
            i += 1
            a[i % len(a)] += 1
            x -= 1

        state = tuple(a)

    # print(res)
    return res


def test():

    assert solve('0 2 7 0') == 5


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

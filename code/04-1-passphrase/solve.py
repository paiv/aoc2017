#!/usr/bin/env python3


def solve(problem):
    data = [line.split() for line in problem.splitlines()]
    return sum(len(row) == len(set(row)) for row in data)


def test():

    assert solve('aa bb cc dd ee') == 1
    assert solve('aa bb cc dd aa') == 0
    assert solve('aa bb cc dd aaa') == 1


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

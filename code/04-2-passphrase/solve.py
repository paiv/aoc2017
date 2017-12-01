#!/usr/bin/env python3


def solve(problem):
    data = (line.split() for line in problem.splitlines())
    data = (row for row in data if len(row) == len(set(row)))
    data = (all(sorted(row[i]) != sorted(row[k]) for i in range(len(row) - 1) for k in range(i + 1, len(row)))
            for row in data)
    return sum(data)


def test():

    assert solve('abcde fghij') == 1
    assert solve('abcde xyz ecdab') == 0
    assert solve('a ab abc abd abf abj') == 1
    assert solve('iiii oiii ooii oooi oooo') == 1
    assert solve('oiii ioii iioi iiio') == 0


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

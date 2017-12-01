#!/usr/bin/env python3


def solve(problem):
    spreadsheet = [[int(x) for x in line.split()] for line in problem.splitlines()]
    return sum(max(row) - min(row) for row in spreadsheet)


def test():

    problem = """
5 1 9 5
7 5 3
2 4 6 8
""".strip()

    assert solve(problem) == 18


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

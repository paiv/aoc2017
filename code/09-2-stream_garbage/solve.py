#!/usr/bin/env python3


def solve(problem):
    res = 0
    level = 0
    state = 0

    for c in problem:

        if state == 0:

            if c == '<':
                level += 1
                state = 1

            elif c == '{':
                level += 1

            elif c == '}':
                level -= 1

        elif state == 1:

            if c == '>':
                level -= 1
                state = 0

            elif c == '!':
                state = 2

            else:
                res += 1

        elif state == 2:

            state = 1


    return res


def test():
    assert solve('<>') == 0
    assert solve('<random characters>') == 17
    assert solve('<<<<>') == 3
    assert solve('<{!>}>') == 2
    assert solve('<!!>') == 0
    assert solve('<!!!>>') == 0
    assert solve('<{o"i!a,<{i<a>') == 10
    assert solve('<{o"i!a,<{i<a>') == 10


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

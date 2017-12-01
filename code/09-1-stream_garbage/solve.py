#!/usr/bin/env python3


def solve(problem):
    res = 0
    level = 0
    state = 0

    for c in problem:

        if state == 0:

            if c == '<':
                state = 1

            elif c == '{':
                level += 1
                res += level

            elif c == '}':
                level -= 1

        elif state == 1:

            if c == '>':
                state = 0

            elif c == '!':
                state = 2

        elif state == 2:

            state = 1


    return res


def test():
    assert solve('{}') == 1
    assert solve('{{{}}}') == 6
    assert solve('{{},{}}') == 5
    assert solve('{{{},{},{{}}}}') == 16
    assert solve('{<a>,<a>,<a>,<a>}') == 1
    assert solve('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert solve('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert solve('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

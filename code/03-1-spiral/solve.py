#!/usr/bin/env python3


def solve0(problem):
    n = int(problem)

    w = 1000
    zx, zy = (w//2, w//2)
    x, y = zx, zy
    # top-left, bottom-right
    toplx,toply = (zx, zy)
    botrx,botry = (zx, zy)

    t = 1

    while t < n:

        botrx += 1
        for i in range(x + 1, botrx + 1):
            x = i
            t += 1
            if t == n:
                break

        if t == n:
            break

        toply -= 1
        for i in range(y - 1, toply - 1, -1):
            y = i
            t += 1
            if t == n:
                break

        if t == n:
            break

        toplx -= 1
        for i in range(x - 1, toplx - 1, -1):
            x = i
            t += 1
            if t == n:
                break

        if t == n:
            break

        botry += 1
        for i in range(y + 1, botry + 1):
            y = i
            t += 1
            if t == n:
                break

        if t == n:
            break

    res = abs(x - zx) + abs(y - zy)
    # print(res, (x,y))
    return res


def solve(problem):
    n = int(problem)

    r = 1
    while r*r < n:
        r += 2

    w = (r - 1) // 2
    x = abs((r * r - n) % (r - 1) - w)
    return w + x


def test():
    assert solve('2') == 1
    assert solve('3') == 2
    assert solve('13') == 4
    assert solve('17') == 4
    assert solve('23') == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

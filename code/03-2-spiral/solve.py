#!/usr/bin/env python3
import numpy as np


def solve(problem):
    n = int(problem)

    w = 1000
    a = np.zeros((w, w), dtype=np.int)
    zx, zy = (w//2, w//2)
    x, y = zx, zy
    # top-left, bottom-right
    toplx,toply = (zx, zy)
    botrx,botry = (zx, zy)

    t = 1
    a[y,x] = t

    def neib(x,y):
        return (a[y-1,x-1] + a[y-1,x] + a[y-1,x+1] +
                a[y  ,x-1] + a[y  ,x] + a[y  ,x+1] +
                a[y+1,x-1] + a[y+1,x] + a[y+1,x+1] )

    while t <= n:

        botrx += 1
        for i in range(x + 1, botrx + 1):
            x = i
            t = neib(x,y)
            a[y,x] = t
            if t > n:
                break

        if t > n:
            break

        toply -= 1
        for i in range(y - 1, toply - 1, -1):
            y = i
            t = neib(x,y)
            a[y,x] = t
            if t > n:
                break

        if t > n:
            break

        toplx -= 1
        for i in range(x - 1, toplx - 1, -1):
            x = i
            t = neib(x,y)
            a[y,x] = t
            if t > n:
                break

        if t > n:
            break

        botry += 1
        for i in range(y + 1, botry + 1):
            y = i
            t = neib(x,y)
            a[y,x] = t
            if t > n:
                break

        if t > n:
            break

    print(t, (x,y))
    return t


def test():
    assert solve('1') == 2
    assert solve('2') == 4
    assert solve('5') == 10
    assert solve('59') == 122
    assert solve('60') == 122
    assert solve('350') == 351


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

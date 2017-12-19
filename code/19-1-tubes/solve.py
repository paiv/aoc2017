#!/usr/bin/env pypy
from __future__ import print_function


def solve(problem):
    b = problem.splitlines()
    w,h = len(b[0]),len(b)

    x = b[0].index('|')
    y = 0
    d = 'down'
    res = ''

    while x >= 0 and x < w and y >= 0 and y < h:
        c = b[y][x]

        if c == ' ':
            break

        if d in ('up', 'down'):

            if c == '+':
                d = 'right' if b[y][x + 1] != ' ' else 'left'
            else:
                if c.isalpha():
                    res += c

        elif d in ('left', 'right'):
            if c == '+':
                d = 'down' if b[y + 1][x] != ' ' else 'up'
            else:
                if c.isalpha():
                    res += c

        if d == 'down':
            y += 1
        elif d == 'up':
            y -= 1
        elif d == 'right':
            x += 1
        elif d == 'left':
            x -= 1

    return res


def test():
    problem = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                
""".strip('\n')

    assert solve(problem) == 'ABCDEF'


def getinput():
    import fileinput
    f = fileinput.input()
    text = ''.join(f).strip('\n')
    f.close()
    return text


if __name__ == '__main__':
    test()
    print(solve(getinput()))

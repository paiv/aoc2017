#!/usr/bin/env python3
import re
import numpy as np


def rect(shape, screen):
    x,y = shape
    t = np.ones((y,x))
    screen[:y, :x] = t
    return screen


def rotate_col(col, n, screen):
    t = screen[:,col]
    t = np.roll(t, n)
    screen[:,col] = t
    return screen


def rotate_row(row, n, screen):
    t = screen[row,:]
    t = np.roll(t, n)
    screen[row,:] = t
    return screen


def display(screen):
    s = '\n'.join(''.join(['#' if c else '.' for c in row]) for row in screen)
    print(s)


command_rx = re.compile(r'rect (\d+)x(\d+)|rotate column x=(\d+) by (\d+)|rotate row y=(\d+) by (\d+)')

def parse_command(text):
    m = command_rx.match(text)

    if m.group(1):
        return ('rect', int(m.group(1)), int(m.group(2)))
    elif m.group(3):
        return ('rx', int(m.group(3)), int(m.group(4)))
    elif m.group(5):
        return ('ry', int(m.group(5)), int(m.group(6)))


def run_commands(screen, text):
    for line in text.splitlines():
        cmd, a, b = parse_command(line)
        if cmd == 'rect':
            rect((a, b), screen)
        elif cmd == 'rx':
            rotate_col(a, b, screen)
        elif cmd == 'ry':
            rotate_row(a, b, screen)


CharTable = """
A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z
....................####.####............###...##.#..#...............................###................................#...#.....
....................#....#................#.....#.#.#................................#..#...............................#...#.....
....................###..###..............#.....#.##.................................#..#................................#.#......
....................#....#................#.....#.#.#................................###..................................#.......
....................#....#................#..#..#.#.#................................#.#..................................#.......
....................####.#...............###..##..#..#...............................#..#.................................#.......
""".strip()

def read_chars(screen):
    charmap = CharTable.splitlines()[1:]
    charmap = [[1 if c == '#' else 0 for c in line] for line in charmap]
    charmap = np.array(charmap, dtype=np.int)
    charmap = np.split(charmap, 26, axis=1)

    screen = np.split(screen, screen.shape[1] // 5, axis=1)
    res = []

    for x in screen:
        for i in range(0, len(charmap)):
            if np.all(charmap[i] == x):
                res.append(chr(ord('A') + i))
                break

    res = ''.join(res)
    return res


def solve(text, shape):
    screen = np.zeros((shape[1], shape[0]), dtype=np.int)
    run_commands(screen, text)
    display(screen)
    # return read_chars(screen)
    return ''


def test():
    pass


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput(), (50, 6)))

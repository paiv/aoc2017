#!/usr/bin/env python3
import base64
import re


def parse_problem(text):
    rx = re.compile(r'^.*?\((.*?)\s*,\s*(.*?)\)')

    text = text.splitlines()[0]

    if not rx.search(text):
        text = base64.b64decode(text).decode('utf-8')

    m = re.sub(rx, r'\1', text)
    k = re.sub(rx, r'\2', text)
    m = base64.b64decode(m)

    return (m, k, text)


def solve(problem):
    msg,key,problem = parse_problem(problem)
    # print(problem)
    # print(msg)
    # print(key)

    def xor(a,b):
        def n(c):
            if isinstance(c, str):
                return ord(c)
            return int(c)

        return [n(a[i]) ^ n(b[i % len(b)]) for i in range(len(a))]

    def sor(a,b):
        return ''.join(chr(x) for x in xor(a,b))

    def rot(text):
        asci = ''.join(chr(ord('a') + i) for i in range(26))
        uasc = asci.upper()
        xx = uasc + asci
        yy = uasc[13:] + uasc[:13] + asci[13:] + asci[:13]
        t = str.maketrans(xx, yy)
        return text.translate(t)

    # return ' '.join('{:02x}'.format(x) for x in msg)

    return rot(sor(msg, base64.b64decode('a29uYW1p')))


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    print(solve(getinput()))

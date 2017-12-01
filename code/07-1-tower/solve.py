#!/usr/bin/env python3
import re


def solve(problem):
    rx = re.compile(r'^(\w+) \((\d+)\)(?: -> (.*?))?$', re.M)

    nodes = set()
    child_nodes = set()

    for n,w,t in rx.findall(problem):
        children = t.split(', ') if t else []
        child_nodes.update(children)
        nodes.add(n)

    root = (nodes - child_nodes).pop()

    return root


def test():
    problem = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip()

    assert solve(problem) == 'tknk'


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

#!/usr/bin/env python3
import subprocess
import re


def render(problem):
    rx = re.compile(r'^(\w+) \((\d+)\)(?: -> (.*?))?$', re.M)
    res = []

    res.append('digraph day7 {')

    for n,w,t in rx.findall(problem):
        res.append('  {} [label="{}\n{}"]'.format(n, n, w))
        children = t.split(', ') if t else []
        for c in children:
            res.append('  {} -> {}'.format(n, c))

    res.append('}')
    return '\n'.join(res)


def viz(problem):
    dot = render(problem)

    subprocess.run('dot -Tpng -o graph.png'.split(), input=dot.encode('ascii'))


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

    viz(problem)



def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    # test()
    viz(getinput())

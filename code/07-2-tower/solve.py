#!/usr/bin/env python3
import re
import statistics


def solve(problem):
    rx = re.compile(r'^(\w+) \((\d+)\)(?: -> (.*?))?$', re.M)

    parents = dict()
    for n,w,t in rx.findall(problem):
        children = t.split(', ') if t else []
        w = int(w)
        for c in children:
            parents[c] = n

    root = n
    while parents.get(root, None):
        root = parents[root]


    graph = dict()
    wei = dict()

    for n,w,t in rx.findall(problem):
        children = t.split(', ') if t else []
        w = int(w)
        wei[n] = w

        for c in children:
            cs = graph.get(n, list())
            cs.append(c)
            graph[n] = cs

    def bal(g, key, xs):
        cs = g.get(key, list())
        y = wei[key] + sum(bal(g, x, xs) for x in cs)
        xs[key] = y
        return y

    summed = dict()
    bal(graph, root, summed)
    print(summed)

    def boo(g, key):
        if key in g:
            n = statistics.median(summed[c] for c in g.get(key, list()))
            for c in g.get(key, list()):
                if summed[c] != n:
                    print(wei[c], summed[c], n)
                    dif = wei[c] - (summed[c] - n)

                    for q in g.get(c, list()):
                        ret = boo(g, q)
                        if ret:
                            return ret

                    return dif

    res = boo(graph, root)
    print(res)
    return res


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

    assert solve(problem) == 60


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

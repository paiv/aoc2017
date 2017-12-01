#!/usr/bin/env python3
from collections import defaultdict


def solve(problem):
    graph = defaultdict(list)

    for line in problem.splitlines():
        p,cs = line.split(' <-> ', 2)
        for c in cs.split(', '):
            graph[int(c)].append(int(p))

    res = 0
    visited = set()
    fringe = list()

    for p in graph:
        if p in visited:
            continue
        res += 1

        fringe.append([p])

        while len(fringe) > 0:
            for p in fringe.pop():
                if p in visited:
                    continue
                visited.add(p)

                fringe.append(graph[p])

    return res


def test():
    problem = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".strip()

    assert solve(problem) == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

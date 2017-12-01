#!/usr/bin/env python3
from collections import defaultdict


def solve(problem):
    graph = defaultdict(list)

    for line in problem.splitlines():
        p,cs = line.split(' <-> ', 2)
        for c in cs.split(', '):
            graph[int(c)].append(int(p))


    visited = set()
    fringe = list()

    fringe.append([0])

    while len(fringe) > 0:
        for p in fringe.pop():
            if p in visited:
                continue
            visited.add(p)

            fringe.append(graph[p])

    res = len(visited)

    return res


def solve2(problem):
    parents = defaultdict(list)

    for line in problem.splitlines():
        a = [x.strip(',') for x in line.split()]
        s = int(a[0])
        for t in map(int, a[2:]):
            parents[t].append(s)


    res = 0

    while len(parents) > 0:
        res += 1

        visited = set()
        fringe = list()

        fringe.append(list(parents.keys())[:1])

        while len(fringe) > 0:
            for p in fringe.pop():
                if p in visited:
                    continue
                visited.add(p)

                fringe.append(parents[p])

        for k in visited:
            del parents[k]


    print(res)
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

    assert solve(problem) == 6
    # assert solve(problem) == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))

from collections import defaultdict
from collections import deque
from os import walk
filename = '../inputs/day23_test.txt'

def build_graph(): 

    edges = [line.strip().split("-") for line in open(filename)]
    """
    for line in f:
        line = line.strip()
        a, b = line.split("-")
        #print(a, b)
        edges.append((a, b))
    """

    graph = defaultdict(list)

    for edge in edges:
        a, b = edge

        graph[a].append(b)
        graph[b].append(a)

    return graph

g = build_graph()



def print_connected_components(g):

    def dfs(node, component):
        if node in visited:
            return
        visited.add(node)
        component.append(node)
        for neighbour in g[node]:
            dfs(neighbour, component)

    visited = set()
    components = []

    for node in g:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    print(components)


def solve(part1):
    if part1:
        sets = set()

        for x in g:
            for y in g[x]:
                for z in g[y]:
                    if x != z and x in g[z]:
                        sets.add(tuple(sorted([x, y, z])))

        print("PART 1", len([s for s in sets if any(cn.startswith("t") for cn in s)]))
    else:
        res = print_connected_components(g)
        print(res)
        print("PART 2")


solve(False)

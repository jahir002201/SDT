import sys

class Edge:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Input number of nodes and edges
n, e = map(int, input().split())

edge_list = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge_list.append(Edge(a, b, c))

# Initialize distances
dis = [sys.maxsize] * n
dis[0] = 0  # assuming 0 as the source node

# Bellman-Ford algorithm
for _ in range(n-1):
    for ed in edge_list:
        if dis[ed.a] != sys.maxsize and dis[ed.a] + ed.c < dis[ed.b]:
            dis[ed.b] = dis[ed.a] + ed.c

# Check for negative weight cycles
cycle = False
for ed in edge_list:
    if dis[ed.a] != sys.maxsize and dis[ed.a] + ed.c < dis[ed.b]:
        cycle = True
        break

# Output results
if cycle:
    print("Negative cycle detected!")
else:
    for i in range(n):
        print(f"{i} -> {dis[i]}")
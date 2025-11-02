# DSU (Disjoint Set Union) with Union by Size and Cycle Detection

def dsu_find(node):
    if parent[node] == -1:
        return node
    parent[node] = dsu_find(parent[node])  # Path compression
    return parent[node]

def dsu_union_by_size(node1, node2):
    leaderA = dsu_find(node1)
    leaderB = dsu_find(node2)
    if leaderA == leaderB:
        return
    if group_size[leaderA] > group_size[leaderB]:
        parent[leaderB] = leaderA
        group_size[leaderA] += group_size[leaderB]
    else:
        parent[leaderA] = leaderB
        group_size[leaderB] += group_size[leaderA]

# Input number of nodes and edges
n, e = map(int, input().split())

# Initialize DSU arrays
parent = [-1] * n
group_size = [1] * n

cycle = False

for _ in range(e):
    a, b = map(int, input().split())
    leaderA = dsu_find(a)
    leaderB = dsu_find(b)
    if leaderA == leaderB:
        cycle = True
    else:
        dsu_union_by_size(a, b)

if cycle:
    print("Cycle Detected.")
else:
    print("No Cycle.")
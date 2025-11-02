import sys

# Input number of nodes and edges
n, e = map(int, input().split())

# Initialize adjacency matrix
adj_mat = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):
    adj_mat[i][i] = 0  # distance to itself is 0

# Read edges
for _ in range(e):
    a, b, c = map(int, input().split())
    adj_mat[a][b] = c

# Floyd-Warshall algorithm
for k in range(n):
    for i in range(n):
        if adj_mat[i][k] == sys.maxsize:
            continue
        for j in range(n):
            if adj_mat[k][j] != sys.maxsize and adj_mat[i][k] + adj_mat[k][j] < adj_mat[i][j]:
                adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j]

# Check for negative cycles
cycle = False
for i in range(n):
    if adj_mat[i][i] < 0:
        cycle = True
        break

# Output results
if cycle:
    print("Negative cycle detected")
else:
    print("Shortest paths between all pairs:")
    for i in range(n):
        for j in range(n):
            if adj_mat[i][j] == sys.maxsize:
                print(f"src->{i} dis->{j} weight: INF", end=", ")
            else:
                print(f"src->{i} dis->{j} weight: {adj_mat[i][j]}", end=", ")
        print()
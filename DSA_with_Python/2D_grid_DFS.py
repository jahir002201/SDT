d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def valid(i, j):
    return 0 <= i < n and 0 <= j < m

def dfs(si, sj):
    print(si, sj)
    vis[si][sj] = True
    for di, dj in d:
        ci, cj = si + di, sj + dj
        if valid(ci, cj) and not vis[ci][cj]:
            dfs(ci, cj)

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

si, sj = map(int, input().split())

vis = [[False]*m for _ in range(n)]

dfs(si, sj)
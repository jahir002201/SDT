from collections import deque

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def valid(i, j):
    return 0 <= i < n and 0 <= j < m

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    vis[si][sj] = True
    dis[si][sj] = 0

    while q:
        a, b = q.popleft()
        for di, dj in d:
            ci, cj = a + di, b + dj
            if valid(ci, cj) and not vis[ci][cj]:
                q.append((ci, cj))
                vis[ci][cj] = True
                dis[ci][cj] = dis[a][b] + 1


n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

si, sj = map(int, input().split())

vis = [[False]*m for _ in range(n)]
dis = [[-1]*m for _ in range(n)]

bfs(si, sj)

print(dis[2][3])
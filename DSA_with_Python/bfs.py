from collections import deque

# Graph representation
v = [[] for _ in range(1005)]
vis = [False] * 1005
parent = [-1] * 1005
level = [0] * 1005

def bfs(src, des):
    q = deque()
    q.append(src)
    vis[src] = True
    level[src] = 0
    parent[src] = -1

    while q:
        par = q.popleft()
        for child in v[par]:
            if not vis[child]:
                q.append(child)
                vis[child] = True
                level[child] = level[par] + 1
                parent[child] = par

    if vis[des]:
        path = []
        x = des
        while x != -1:
            path.append(x)
            x = parent[x]
        path.reverse()
        print(" ".join(map(str, path)))
    else:
        print(f"No path from {src} to {des}")


n, e = map(int, input().split())
for _ in range(e):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

src, des = map(int, input().split())
bfs(src, des)
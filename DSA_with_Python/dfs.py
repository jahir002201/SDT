v = [[] for _ in range(1005)]
vis = [False] * 1005

def dfs(src):
    print(src)
    vis[src] = True
    for child in v[src]:
        if not vis[child]:
            dfs(child)


n, e = map(int, input().split())
for _ in range(e):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

dfs(0)
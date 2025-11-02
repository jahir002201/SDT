import sys
sys.setrecursionlimit(10**6)

# Graph representation
adj_list = [[] for _ in range(100005)]
visited = [False] * 100005
parent = [-1] * 100005
cycle = False

def dfs(src):
    global cycle
    visited[src] = True
    for child in adj_list[src]:
        if visited[child] and parent[src] != child:
            cycle = True
            return
        if not visited[child]:
            parent[child] = src
            dfs(child)
            if cycle:
                return


n, e = map(int, input().split())
for _ in range(e):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * n
parent = [-1] * n
cycle = False

for i in range(n):
    if not visited[i]:
        dfs(i)
        if cycle:
            break

if cycle:
    print("Cycle Detected")
else:
    print("No Cycle")
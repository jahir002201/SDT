from collections import deque

# Graph representation
adj_list = [[] for _ in range(100005)]
visited = [False] * 100005
parent = [-1] * 100005
cycle = False

def bfs(src):
    global cycle
    q = deque()
    q.append(src)
    visited[src] = True
    parent[src] = -1

    while q:
        par = q.popleft()
        for child in adj_list[par]:
            if visited[child] and parent[par] != child:
                cycle = True
                return
            if not visited[child]:
                visited[child] = True
                parent[child] = par
                q.append(child)


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
        bfs(i)
        if cycle:
            break

if cycle:
    print("Cycle Detected")
else:
    print("No Cycle")
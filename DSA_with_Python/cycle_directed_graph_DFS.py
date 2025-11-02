import sys
sys.setrecursionlimit(10**6)

# Graph representation
adj_list = [[] for _ in range(100005)]
visited = [False] * 100005
pathVisited = [False] * 100005
cycle = False

def dfs(src):
    global cycle
    visited[src] = True
    pathVisited[src] = True

    for child in adj_list[src]:
        if visited[child] and pathVisited[child]:
            cycle = True
        if not visited[child]:
            dfs(child)
    
    pathVisited[src] = False


n, e = map(int, input().split())
for _ in range(e):
    a, b = map(int, input().split())
    adj_list[a].append(b)

visited = [False] * n
pathVisited = [False] * n
cycle = False

for i in range(n):
    if not visited[i]:
        dfs(i)

if cycle:
    print("Cycle Detected")
else:
    print("No Cycle")
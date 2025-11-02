from collections import deque
import sys

n, e = map(int, input().split())
adj_list = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

dis = [sys.maxsize] * n

def dijkstra(src):
    q = deque()
    q.append((src, 0))
    dis[src] = 0
    while q:
        par_node, par_dis = q.popleft()
        for child_node, child_dis in adj_list[par_node]:
            if par_dis + child_dis < dis[child_node]:
                dis[child_node] = par_dis + child_dis
                q.append((child_node, dis[child_node]))

dijkstra(0)

for i in range(n):
    print(f"{i} -> {dis[i]}")
import heapq

pq = []
heapq.heappush(pq, -10)
heapq.heappush(pq, -30)
heapq.heappush(pq, -20)

print(-pq[0])  # 30
heapq.heappop(pq)
print(-pq[0])  # 20
import heapq
INF = int(1e9)

def dijkstra(start, adj):
    dist = [INF]*(N+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d: continue
        for edge in adj[u]:
            w, v = edge
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    return dist

N, M, P = map(int, input().split())
adj1 = [[]*(N+1) for _ in range(N+1)] # 순방향 인접 리스트
adj2 = [[]*(N+1) for _ in range(N+1)] # 역방향 인접 리스트
for _ in range(M):
    u, v, w = map(int, input().split())
    adj1[u].append((w, v))
    adj2[v].append((w, u)) # 도착지에서부터 역순으로 추적하기 위해 간선의 방향을 바꿈
dist1 = dijkstra(P, adj1)
dist2 = dijkstra(P, adj2)
answer = 0
for i in range(1, N+1):
    cost = dist1[i]+dist2[i]
    if cost > answer:
        answer = cost
print(answer)
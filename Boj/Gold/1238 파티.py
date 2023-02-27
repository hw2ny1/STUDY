import heapq
import sys
input = sys.stdin.readline
inf = 1e8

N, M, X = map(int,input().split())
roads = [[] for _ in range(N+1)]

for _ in range(M):
    x,y,fee = map(int,input().split())
    heapq.heappush(roads[x],(fee,y))

def dijkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))
    dist = [inf] * (N+1)
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue
        for road in roads[now]:
            fee = cost + road[0]
            if fee < dist[road[1]]:
                dist[road[1]] = fee
                heapq.heappush(q,(fee,road[1]))
    return dist[end]

temp = 0
for i in range(1,N+1):
    temp = max(dijkstra(i,X)+dijkstra(X,i),temp)
print(temp)
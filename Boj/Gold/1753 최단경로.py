inf = 1e8
import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
route = [[] for _ in range(V+1)]
min_dist = [inf for _ in range(V+1)]

for _ in range(E):
    x,y,z = map(int,input().split())
    route[x].append([z,y])

def dijckstra(start):
    q = []
    heapq.heappush(q,[0,start])
    min_dist[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if min_dist[now] < dist:
            continue
        for nex in route[now]:
            cost = min_dist[now] + nex[0]
            if min_dist[nex[1]] > cost:
                min_dist[nex[1]] = cost
                heapq.heappush(q , [cost, nex[1]])

dijckstra(start)

for i in range(1,V+1):
    if min_dist[i] == inf:
        min_dist[i] = 'INF'
    print(min_dist[i])
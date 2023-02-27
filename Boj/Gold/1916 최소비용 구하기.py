import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

N = int(input())
M = int(input())
bus_stop = [list() for _ in range(N+1)]
mindist = [inf for _ in range(N+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    mindist[start] = inf
    while q:
        dist, now = heapq.heappop(q)
        if dist > mindist[now]:
            continue
        for bus in bus_stop[now]:
            cost = dist + bus[0]
            if mindist[bus[1]] > cost:
                mindist[bus[1]] = cost
                heapq.heappush(q,(cost,bus[1]))

for _ in range(M):
    a,b,c = map(int,input().split())
    bus_stop[a].append((c,b))

start,end = map(int,input().split())
dijkstra(start)
print(mindist[end])
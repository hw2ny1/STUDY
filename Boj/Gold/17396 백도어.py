import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    min_dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if min_dist[now] < cost:
            continue
        for next, fee in roads[now]:
            tot = fee + cost #min_dist[now] 도 되지만 cost라 넣을때 더 빠름
            if not w[next]:
                if tot < min_dist[next]:
                    min_dist[next] = tot
                    heapq.heappush(q,(tot,next)) # cost를 넣을려면 tot가 들어가야함


N, M = map(int, input().split())
w = list(map(int, input().split()))
w[-1] = 0
roads = [[] for _ in range(N)]
min_dist = [inf for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

dijkstra(0)
print(min_dist[N-1]) if min_dist[N-1] != inf else print(-1)
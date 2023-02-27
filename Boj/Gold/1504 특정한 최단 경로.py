import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

N, E = map(int,input().split())
road = [[] for _ in range(N+1)]


def dijckstra(start):
    mindist = [inf for _ in range(N+1)]
    mindist[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist < mindist[now]:
            continue
        for fee in road[now]:
            cost = fee[0] + mindist[now]
            if mindist[fee[1]] > cost:
                mindist[fee[1]] = cost
                heapq.heappush(q , [mindist[fee[1]], fee[1]])
    return mindist

for _ in range(E):
    a,b,c = map(int,input().split())
    road[a].append([c,b])
    road[b].append([c,a])

v1, v2 = map(int,input().split())
one = dijckstra(1)
v1_ = dijckstra(v1)
v2_ = dijckstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(cnt if cnt < inf else -1)
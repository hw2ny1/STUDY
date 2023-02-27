import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int,input().split())  # N : 도시의 수, M : 고속도로의 수, K : 햇수
A, B = map(int,input().split())     # A 에서 B로 가는 길

inf = 1e8
min_dist = [inf for _ in range(N+1)]
highway = [[] for _ in range(N+1)]

for _ in range(M):
    f, t, c = map(int,input().split())  # f 에서 t로 가는 비용 c
    highway[f].append([t,c])

def dijckstra(A,highway):
    q = []
    heapq.heappush(q,(A,0))
    min_dist[A] = inf

    while q:
        now, dist = heapq.heappop(q)
        if min_dist[now] < dist:
            continue
        for way in highway[now]:
            fee = dist + way[1]
            if fee < min_dist[way[0]]:
                min_dist[way[0]] = fee
                heapq.heappush(q,(way[0],fee))

dijckstra(A,highway)
print(min_dist[B])
k = 0

for _ in range(K):
    min_dist = [inf for _ in range(N+1)]
    k = int(input())
    for way in highway:
        for i in way:
            i[1] += k
    dijckstra(A,highway)
    print(min_dist[B])
import sys
input = sys.stdin.readline
import heapq
from collections import deque
inf = 1e8

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    r_graph = [[] for _ in range(N)]
    min_dist = [inf for _ in range(N)]
    ban_line = set()

    for _ in range(M):
        a, b, c = map(int,input().split())
        graph[a].append([c,b])
        r_graph[b].append([c,a])


    def bfs(start,end):
        q = deque()
        q.append(end)
        while q:
            now = q.popleft()
            if now == start:
                continue
            for cost, next in r_graph[now]:
                if min_dist[now] - min_dist[next] == cost:
                    if (next, now) not in ban_line:
                        ban_line.add((next, now))
                        q.append((next))


    def dijkstra(start):
        q = []
        q.append((0, start))
        min_dist[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if min_dist[now] < dist:
                continue
            for cost, next in graph[now]:
                if (now, next) in ban_line:continue
                total_dist = dist + cost
                if min_dist[next] > total_dist:
                    min_dist[next] = total_dist
                    heapq.heappush(q,(total_dist, next))


    dijkstra(S)
    bfs(S,D)
    min_dist = [inf for _ in range(N)]
    dijkstra(S)
    if min_dist[D] < 1e8:
        print(min_dist[D])
    else:
        print(-1)

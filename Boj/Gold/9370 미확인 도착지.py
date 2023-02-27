import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(start):
    min_dist = [inf for _ in range(node + 1)]
    min_dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > min_dist[now]:
            continue
        for road in roads[now]:
            cost = road[0] + dist
            if cost < min_dist[road[1]]:
                min_dist[road[1]] = cost
                heapq.heappush(q,(cost,road[1]))
    return min_dist


T = int(input())
for _ in range(T):
    node, road_N, case = map(int, input().split())
    start, need_1, need_2 = map(int, input().split())
    roads = [[] for _ in range(node+1)]
    pilsu = 0
    for _ in range(road_N):
        a, b, cost = map(int, input().split())
        roads[a].append([cost, b])
        roads[b].append([cost, a])
        if (a == need_1 and b == need_2) or (a == need_2 and b == need_1):
            pilsu = cost
    start_min_dist = dijkstra(start)
    need_1_min_dist = dijkstra(need_1)
    need_2_min_dist = dijkstra(need_2)
    temp = []
    for _ in range(case):
        hubo = int(input())
        if min(start_min_dist[need_1] + need_2_min_dist[hubo] + pilsu , start_min_dist[need_2] + need_1_min_dist[hubo] + pilsu) <= start_min_dist[hubo]:
            temp.append(hubo)
    temp.sort()
    print(*temp)
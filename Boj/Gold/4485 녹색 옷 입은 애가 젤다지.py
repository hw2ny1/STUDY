import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dijkstra(min_dist):
    q = [(graph[0][0], 0, 0)]
    min_dist[0][0] = graph[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if min_dist[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:continue
            total_cost = dist + graph[nx][ny]
            if min_dist[nx][ny] > total_cost:
                min_dist[nx][ny] = total_cost
                heapq.heappush(q,(total_cost, nx, ny))
    return min_dist[N-1][N-1]

t = 0
while True:
    t+=1
    N = int(input())
    if N == 0:break
    graph = [list(map(int, input().split())) for _ in range(N)]
    min_dist = [[inf for _ in range(N)] for _ in range(N)]
    print(f'Problem {t}:',dijkstra(min_dist))
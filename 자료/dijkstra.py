import sys
inf = sys.maxsize

def min_index(list):
    temp, index = inf, 0
    for i in range(len(list)):
        if list[i] < temp:
            temp = list[i]
            index = i
    return i

def dijkstra(now):
    visited[now] = True
    for i in road[now]:
        min_num = min_index(road[now])
        if min_dist[i] > road[now]

min_dist = [inf] * N
visited = [False] * N
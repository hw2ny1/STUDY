from collections import deque
from sys import stdin
input = stdin.readline

def bfs(start, graph):
    visited[1] = 1
    q = deque([[start, 1]])
    while q:
        now, flag = q.popleft()
        if flag == 1:
            blue.add(now)
        elif flag == 2:
            white.add(now)
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 2//flag
                q.append([next, 2//flag])

V = int(input())
graph = [[] for _ in range(V+1)]
visited = [0] * (V + 1)
flag = 0
blue = set()
white = set()
for n in range(1,V+1):
    arr = list(map(int,input().split()))
    for i in range(arr[0]):
        graph[n].append(arr[i+1])

for i in range(1, V+1):
    if not visited[i]:
        bfs(i, graph)

print(len(blue))
print(*blue)
print(len(white))
print(*white)
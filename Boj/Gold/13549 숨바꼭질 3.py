from collections import deque
import sys
input = sys.stdin.readline
inf = 100001
visited = [[-1,0] for _ in range(inf)]


def BFS(start,end):
    visited[start][0] = 0
    visited[start][1] = 0
    q = deque([start])
    while q:
        now = q.popleft()
        temp = now*2
        if now == end and visited[now][1] < visited[end][1]:
            visited[end][1] = visited[now][1]
        if inf > temp >= 0:
            if visited[temp][0] == -1:
                visited[temp][0] = visited[now][0]
                visited[temp][1] = visited[now][1]
                q.append(temp)
        for i in (now-1,now+1):
            if inf > i >= 0:
                if visited[i][0] == -1:
                    visited[i][0] = visited[now][0]
                    visited[i][1] = visited[now][1] + 1
                    q.append(i)
        

start,end = map(int,input().split())

BFS(start,end)
print(visited[end][1])

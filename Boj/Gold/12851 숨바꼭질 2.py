from collections import deque
import sys
input = sys.stdin.readline

visited = [[-1,0] for _ in range(100001)]
start, end = map(int,input().split())

def BFS(start):
    visited[start][0] = 0
    visited[start][1] = 1
    q = deque([start])
    while q:
        via = q.popleft()
        for i in (via*2,via+1,via-1):
            if i >= 0 and i < 100001:
                if visited[i][0] == -1:
                    visited[i][0] = visited[via][0] + 1
                    visited[i][1] = visited[via][1]
                    q.append(i)
                elif visited[i][0] == visited[via][0] + 1:
                    visited[i][1] += visited[via][1]
BFS(start)
print(visited[end][0])
print(visited[end][1])
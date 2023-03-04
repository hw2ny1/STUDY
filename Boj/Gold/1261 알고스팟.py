from collections import deque
from sys import stdin
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
col, row = map(int,input().split())
maze = [list(input().strip()) for _ in range(row)]
dist = [[-1 for _ in range(col)] for _ in range(row)]

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= row or ny < 0 or ny >= col:continue
        if dist[nx][ny] == -1:
            if maze[nx][ny] == '0':
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx,ny))
            if maze[nx][ny] == '1':
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

print(dist[row-1][col-1])

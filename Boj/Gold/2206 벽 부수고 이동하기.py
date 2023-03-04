import sys
from collections import deque
from sys import stdin
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
row, col = map(int, input().split())
maze = [list(input().strip()) for _ in range(row)]
visited = [[[0]*2 for _ in range(col)]for _ in range(row)]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == row-1 and y == col-1:
            return visited[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:continue
            if visited[nx][ny][w] == 0:
                if maze[nx][ny] == '0':
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx,ny,w))
                elif w == 0 and maze[nx][ny] == '1':
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    q.append((nx,ny,1))
    return -1


print(bfs())
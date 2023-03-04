from sys import stdin
input = stdin.readline
from collections import deque

row, col, k = map(int,input().split())
maze = [list(input().strip()) for _ in range(row)]
visited = [[[0 for _ in range(col)] for _ in range(row)] for _ in range(k+1)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == row-1 and y == col-1:
            return visited[w][x][y]
        for z in range(4):
            nx = x + dx[z];ny = y + dy[z]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:continue
            if maze[nx][ny] == '0' and not visited[w][nx][ny]:
                visited[w][nx][ny] = visited[w][x][y] + 1
                q.append((nx,ny,w))
            if w + 1 <= k and maze[nx][ny] == '1' and not visited[w+1][nx][ny]:
                visited[w+1][nx][ny] = visited[w][x][y] + 1
                q.append((nx,ny,w+1))
    return -1

print(bfs())
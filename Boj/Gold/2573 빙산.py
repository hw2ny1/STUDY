from collections import deque
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
sea = [list(map(int,input().split())) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def melting():
    q = deque()
    p = []
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        temp = 0
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if not sea[nx][ny]:
                temp += 1
        p.append([x, y, temp])

    while p:
        x, y, temp = p.pop()
        sea[x][y] -= temp
        if sea[x][y] < 0:
            sea[x][y] = 0


def bfs(x,y):
    global visited
    q = deque([[x,y]])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:continue
            if sea[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True


def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not sea[i][j]:continue
            if visited[i][j]:continue
            bfs(i,j)
            cnt += 1
    return cnt


c = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    c += 1
    melting()
    cnt = check()
    if cnt > 1:
        print(c)
        break
    elif cnt == 0:
        print(0)
        break

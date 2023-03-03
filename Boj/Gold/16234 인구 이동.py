from sys import stdin
input = stdin.readline
from collections import deque

N, L, R = map(int, input().split())
nara = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0];dy = [0, 0, 1, -1]


def check(x, y):
    q = deque()
    q.append((x,y))
    history = [(x,y)]
    temp = nara[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:continue
            if visited[nx][ny]:continue
            if (nx, ny) not in history and L <= abs(nara[x][y] - nara[nx][ny]) <= R:
                visited[nx][ny] = True
                history.append((nx, ny))
                q.append((nx, ny))
                temp += nara[nx][ny]
    if len(history) == 1:
        return 0
    else:
        temp //= len(history)
        for x, y in history:
            nara[x][y] = temp
        return 1

count = 0
while True:
    flag = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y]:continue
            flag += check(x,y)
    if not flag:
        break
    else:
        count += 1
print(count)
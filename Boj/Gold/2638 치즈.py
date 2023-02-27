import sys
sys.setrecursionlimit(1000000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    paper[x][y] = 2
    for i in range(4):
        DX = x + dx[i]
        DY = y + dy[i]
        if 0 <= DX < N and 0 <= DY < M:
            if paper[DX][DY] == 0:
                bfs(DX, DY)


def bfs_clear(x, y):
    paper[x][y] = 0
    for i in range(4):
        DX = x + dx[i]
        DY = y + dy[i]
        if 0 <= DX < N and 0 <= DY < M:
            if paper[DX][DY] == 2 or paper[DX][DY] == 3:
                bfs_clear(DX, DY)


N, M = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0

while True:
    bfs(0, 0)
    temp_total = 0
    for x in range(1,N-1):
        for y in range(1,M-1):
            temp = 0
            if paper[x][y] == 1:
                temp_total += 1
                for z in range(4):
                    DX = x + dx[z]
                    DY = y + dy[z]
                    if paper[DX][DY] == 2:
                        temp += 1
                if temp >= 2:
                    paper[x][y] = 3
    if temp_total == 0:
        break
    bfs_clear(0, 0)
    cnt += 1

print(cnt)
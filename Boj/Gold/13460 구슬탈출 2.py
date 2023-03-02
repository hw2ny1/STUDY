from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
row, col = map(int,input().split())
board = [list(input().strip()) for _ in range(row)]
visited = [[[[False for _ in range(col)] for _ in range(row)] for _ in range(col)] for _ in range(row)]
q = deque()


def init():
    rx,ry,bx,by = 0,0,0,0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    ct = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx;y += dy;ct += 1
    return x, y, ct


def bfs():
    init()
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(cnt)
                return
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx,next_ry,next_bx,next_by,cnt+1))
    print(-1)


bfs()

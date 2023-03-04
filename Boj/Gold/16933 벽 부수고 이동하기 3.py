from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
    q = deque()
    q.append((0,0,0))
    ans = 1
    time = True
    while q:
        for _ in range(len(q)):
            x, y, w = q.popleft()

            if x == row-1 and y == col-1:
                print(ans)
                return

            for z in range(4):
                nx = x + dx[z];ny = y + dy[z]
                if nx < 0 or nx >= row or ny < 0 or ny >= col or visited[nx][ny] <= w:
                    continue

                if maze[nx][ny] == '0':
                    visited[nx][ny] = w
                    q.append((nx,ny,w))
                if w + 1 <= k and maze[nx][ny] == '1':
                    if not time:
                        q.append((x,y,w))
                    elif time:
                        visited[nx][ny] = w
                        q.append((nx,ny,w+1))
        time = not time
        ans += 1
    print(-1)
    return


row, col, k = map(int,input().split())
maze = [list(input().strip()) for _ in range(row)]
visited = [[k+1 for _ in range(col)] for _ in range(row)]
visited[0][0] = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
bfs()
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(S):
    q = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if virus[i][j] != 0:
                q.append((virus[i][j], i, j, 0))
                visited[i][j] = True
    q.sort()
    q = deque(q)
    while q:
        vn, x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and time+1 <= S:
                    visited[nx][ny] = True
                    virus[nx][ny] = vn
                    q.append((vn, nx, ny, time + 1))


N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

BFS(S)
print(virus[X-1][Y-1])
import sys
input = sys.stdin.readline
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
sys.setrecursionlimit(10**9)


def DFS(x,y):
    che[x][y] = 2
    for dx, dy in direct:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < raw and 0 <= ny < col:
            if che[nx][ny] == 0:
                DFS(nx,ny)


def DFS_2(x,y):
    che[x][y] = 0
    for dx, dy in direct:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < raw and 0 <= ny < col:
            if che[nx][ny] == 2:
                DFS_2(nx,ny)


def pronounce(x,y):
    for dx, dy in direct:
        nx = x + dx
        ny = y + dy
        if che[nx][ny] == 2:
            return True
    return False


raw, col = map(int,input().split())
che = [list(map(int,input().split())) for _ in range(raw)]

history = []
while True:
    DFS(0, 0)
    temp = 0
    for i in range(1,raw-1):
        for j in range(1,col-1):
            if che[i][j] == 1 and pronounce(i,j):
                temp += 1
                che[i][j] = 0
    DFS_2(0, 0)
    if temp > 0:
        history.append(temp)
    else:
        break

print(len(history))
print(history[-1])
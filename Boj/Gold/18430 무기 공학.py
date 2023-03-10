import sys
input = sys.stdin.readline
dir = [[(1,0),(0,0),(0,0),(0,1)],[(1,0),(0,0),(0,0),(0,-1)],
       [(-1,0),(0,0),(0,0),(0,1)],[(-1,0),(0,0),(0,0),(0,-1)]]
check = [[(1,0),(0,0),(0,1)],[(1,0),(0,0),(0,-1)],
       [(-1,0),(0,0),(0,1)],[(-1,0),(0,0),(0,-1)]]

ans = 0
row, col = map(int, input().split())
namu = [list(map(int,input().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]

def promising(x, y, k):
    for dx, dy in check[k]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= row or ny < 0 or ny >= col:
            return False
        if visited[nx][ny]:
            return False
    return True


def summary(x, y, k):
    temp = 0
    for dx, dy in dir[k]:
        nx = x + dx
        ny = y + dy
        temp += namu[nx][ny]
    return temp


def back_tacking(x, y, total):
    global ans
    if y == col:y = 0;x += 1
    if x == row:
        ans = max(ans, total)
        # for vi in visited:
        #     print(*vi)
        # print('---------------')
        return
    for k in range(4):
        if promising(x,y,k):
            for dx,dy in check[k]:
                visited[x+dx][y+dy] = True
            back_tacking(x, y+1, total+summary(x, y, k))
            for dx,dy in check[k]:
                visited[x+dx][y+dy] = False
    back_tacking(x, y+1, total)


back_tacking(0,0,0)
print(ans)



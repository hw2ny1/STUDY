import sys
input = sys.stdin.readline

dx = [-1,0, 1, 0]
dy = [0,-1,0,1]


tone = [[(-1,0),(-2,0,0.05),(-1,-1,0.1),(-1,1,0.1),(0,-1,0.07),(0,-2,0.02),(0,1,0.07),(0,2,0.02),(1,-1,0.01),(1,1,0.01)],
        [(0,-1),(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01)],
        [(1,0),(2,0,0.05),(1,-1,0.1),(1,1,0.1),(0,-1,0.07),(0,-2,0.02),(0,1,0.07),(0,2,0.02),(-1,-1,0.01),(-1,1,0.01)],
        [(0,1),(0,2,0.05),(1,1,0.1),(-1,1,0.1),(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01)]]


def tototo():
    tx, ty = N // 2, N // 2
    l, d = 1, 1
    while True:
        for _ in range(2):
            for _ in range(l):
                tx += dx[d]
                ty += dy[d]
                if 0 <= tx < N and 0 <= ty < N:
                    temp = arr[tx][ty]
                    for i in range(1, 10):
                        x, y, ratio = tone[d][i]
                        nx = tx + x
                        ny = ty + y
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += int(temp * ratio)
                            arr[tx][ty] -= int(temp * ratio)
                        else:
                            arr[tx][ty] -= int(temp * ratio)
                    x, y = tone[d][0]
                    nx = tx + x
                    ny = ty + y
                    if 0 <= nx < N and 0 <= ny < N:
                        arr[nx][ny] += arr[tx][ty]
                        arr[tx][ty] = 0
                    else:
                        arr[tx][ty] = 0
                if tx == 0 and ty == 0:
                    temp = 0
                    for ar in arr:
                        temp += sum(ar)
                    return temp
            d = (d + 1) % 4
        l += 1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
total = 0

for ar in arr:
    total += sum(ar)

print(total-tototo())

def slice(x,y,n):
    global blue, white
    c = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != c:
                slice(x, y, n // 2)
                slice(x + n // 2, y, n // 2)
                slice(x, y + n // 2, n // 2)
                slice(x + n // 2, y + n // 2, n // 2)
                return
    if c == 1:
        blue += 1
    else:
        white += 1


N = int(input())
blue = 0
white = 0
graph = [list(map(int,input().split())) for _ in range(N)]

slice(0,0,N)
print(white)
print(blue)
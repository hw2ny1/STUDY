def slice(x,y,n):
    global result
    c = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != c:
                result += '('
                slice(x, y, n // 2)
                slice(x, y + n // 2, n // 2)
                slice(x + n // 2, y, n // 2)
                slice(x + n // 2, y + n // 2, n // 2)
                result += ')'
                return
    if c == '1':
        result += '1'
    else:
        result += '0'

N = int(input())
result = ''
graph = [list(input()) for _ in range(N)]

slice(0,0,N)
print(result)
N,K = map(int,input().split())
image = [list(map(int,input().split())) for _ in range(N)]

for _ in range(K):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = image[i][j]
    image = temp

for i in range(N):
    print(*image[i])

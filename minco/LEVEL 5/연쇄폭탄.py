N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
def boom(field,cnt):
    for k in range(1,N*N+1):
        cnt_1 = 0
        for i in range(N):
            for j in range(N):
                if field[i][j] == 0:
                    cnt_1 += 1
                if field[i][j] == k:
                    field[i][j] = 0
                    if i < N-1:
                        field[i+1][j] = 0
                    if i > 0:
                        field[i-1][j] = 0
                    if j < N-1:
                        field[i][j+1] = 0
                    if j > 0:
                        field[i][j-1] = 0
        cnt += 1
        if cnt_1 == N*N:
            return cnt -1
    return N*N

print(f'{boom(field,cnt)}초')
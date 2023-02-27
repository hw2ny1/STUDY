N = int(input())
acre = [[0 for _ in range(3)] for _ in range(3)]
loca = []

for i in range(N):
    x,y,plant = map(int,input().split())
    acre[x][y] = plant
    loca.append((x,y))

M = int(input())
wind = list(map(int,input().split()))

for i in range(M):
    for j in range(N):
        if acre[loca[j][0]][loca[j][1]]%10 > wind[i]:
            acre[loca[j][0]][loca[j][1]] -= wind[i]
        elif acre[loca[j][0]][loca[j][1]]%10 <= wind[i]:
            acre[loca[j][0]][loca[j][1]] = acre[loca[j][0]][loca[j][1]]//10

cnt = 0
for i in range(3):
    for j in range(3):
        while acre[i][j] != 0:
            cnt += 1
            acre[i][j] = acre[i][j]//10
print(cnt)

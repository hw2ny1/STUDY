n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
beat_arr = [list(map(int,input().split())) for _ in range(n)]
reco = []

for i in range(n):
    for j in range(n):
        if beat_arr[i][j] == 1:
            reco.append(arr[i][j])

reco_temp = []

for i in reco:
    reco_temp.append((i,reco.count(i)))

reco_temp.sort(key=lambda x: (-x[1], x[0]))

for i in range(len(reco_temp)):
    print(reco_temp[i][0],end=' ')
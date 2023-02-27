arr = [list(map(int,input().split())) for _ in range(4)]
memo_1 = []
memo_2 = []

# 가로
for i in range(4):
    arr[i].count(0)
    if arr[i].count(0) == 0:
        memo_1.append(i)
# 세로
for j in range(8):
    cnt = 0
    for i in range(4):
        if arr[i][j] != 0:
            cnt +=1
    if cnt == 4:
        
        memo_2.append(j)

sum_bin = []
temp = 0
# 가로
for i in memo_1:
    temp += sum(arr[i])
sum_bin.append(temp)
temp = 0
memo_2.append(0)
# 세로
for i in range(len(memo_2)-1):
    if memo_2[i]+1 == memo_2[i+1]:
        for j in range(4):
            temp += arr[j][memo_2[i]]
    if memo_2[i]+1 != memo_2[i+1]:
        for j in range(4):
            temp += arr[j][memo_2[i]]
        sum_bin.append(temp)
        temp = 0
print(max(sum_bin))
N = int(input()) - 3
numlist = list(map(int,input().split()))
i = 0
minresult = 50
while N-i:
    temp = 0
    for j in range(i,i+4):
        temp += numlist[j]
    minresult = min(temp,minresult)
    i += 1
print(minresult)
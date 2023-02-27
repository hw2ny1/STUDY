import sys
input = sys.stdin.readline
inf = 1e10
N = int(input())
num = list(map(int,input().split()))
num.sort()

def binary_serch(binary,target):
    end = len(binary)-1
    start = 0
    while start <= end:
        mid = (start+end)//2
        if -target > binary[mid]:
            start = mid +1
        else:
            end = mid -1
    if mid+1 < N-1 and abs(target+binary[mid]) > abs(target+binary[mid+1]):
        return binary[mid+1]
    else:
        return binary[mid]

temp = inf
if num[N-1] < 0:
    result = [num[N-2],num[N-1]]
elif num[0] > 0:
    result = [num[0],num[1]]
else:
    for i in range(N):
        temp_2 = binary_serch(num,num[i])
        if temp > abs(num[i]+temp_2) and num[i] != temp_2:
            temp = min(temp,abs(num[i]+temp_2),abs(num[i]+temp_2))
            result = [num[i],temp_2]
result.sort()
print(*result)
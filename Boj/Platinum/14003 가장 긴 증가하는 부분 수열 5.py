def binary_search(target,len_list,list):
    start, mid = 0, 0
    end = len_list
    while start < end:
        mid = (start+end)//2
        if list[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
result = [num_list[0]]
check = [0]*N
cnt = 0
for i in range(N):
    if result[-1] < num_list[i]:
        result.append(num_list[i])
        cnt += 1
        check[i] = cnt
    else:
        temp = binary_search(num_list[i],cnt,result)
        result[temp] = num_list[i]
        check[i] = temp

print(cnt+1)
for i in range(N-1,-1,-1):
    if check[i] == cnt:
        result[cnt] = num_list[i]
        cnt -= 1
print(*result)
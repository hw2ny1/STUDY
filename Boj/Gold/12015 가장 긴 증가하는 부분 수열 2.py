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
cnt = 0
for num in num_list:
    if result[-1] < num:
        result.append(num)
        cnt += 1
    else:
        temp = binary_search(num,cnt,result)
        result[temp] = num

print(cnt+1)
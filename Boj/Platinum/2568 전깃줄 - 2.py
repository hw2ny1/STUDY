import sys
input = sys.stdin.readline


def binary_search(x):
    start, mid = 0, 0
    end = len(dp)-1
    while start <= end:
        mid = (start + end)//2
        if dp[mid][0] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return start

N = int(input())
line = []
result = [0]
for _ in range(N):
    x,y = map(int,input().split())
    line.append((x,y))
line.sort()
dp = [(line[0][1],line[0][0])]
cnt = 1
for i in range(1,N):
    if line[i][1] > dp[-1][0]:
        result.append(len(dp))
        dp.append((line[i][1],line[i][0]))
        cnt += 1
    else:
        temp = binary_search(line[i][1])
        dp[temp] = (line[i][1], line[i][0])
        result.append(temp)
print(N-len(dp))
cnt -= 1
for i in range(len(result)-1,-1,-1):
    if result[i] == cnt:
        cnt -= 1
    else:
        result[i] = -1
for i in range(len(result)):
    if result[i] == -1:
        print(line[i][0])
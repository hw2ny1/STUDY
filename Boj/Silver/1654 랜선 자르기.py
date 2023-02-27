import sys
input = sys.stdin.readline


def binary_search(target):
    start = 1
    end = max(line)
    while start <= end:
        mid = (start+end)//2
        temp = 0
        for l in line:
            temp += l//mid
        if temp < target:
            end = mid - 1
        elif temp >= target:
            start = mid + 1
    return end


K, N = map(int,input().split())
line = []
for _ in range(K):
    line.append(int(input()))
print(binary_search(N))
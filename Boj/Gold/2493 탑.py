import sys
input = sys.stdin.readline

N = int(input())
top_list = list(map(int, input().split()))
result = [0 for _ in range(N+1)]
q = []
for i in range(N-1, -1,-1):
    if q:
        while q and q[-1][0] < top_list[i]:
            temp,x = q.pop()
            result[x] = i+1
    if top_list[i] < top_list[i-1]:
        result[i] = i
    else:
        q.append((top_list[i],i))
result.pop()
print(*result)
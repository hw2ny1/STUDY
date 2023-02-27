N = int(input())
lst = list(map(int,input().split()))
NGE = [-1] * (N);q = []
for i in range(N-1,-1,-1):
    while q:
        if q[-1] > lst[i]:
            NGE[i] = q[-1]
            break
        else:
            q.pop()
    q.append(lst[i])
print(*NGE)

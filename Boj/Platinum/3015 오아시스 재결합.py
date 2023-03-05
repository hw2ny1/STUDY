from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())
oasis = deque()
ans = 0
for _ in range(N):
    k = int(input())

    while oasis and oasis[-1][0] < k:
        ans += oasis.pop()[1]

    if not oasis:
        oasis.append((k,1))
        continue

    if oasis[-1][0] == k:
        cnt = oasis.pop()[1]
        ans += cnt

        if oasis:
            ans += 1
        oasis.append((k,cnt+1))

    else:
        oasis.append((k,1))
        ans += 1

print(ans)
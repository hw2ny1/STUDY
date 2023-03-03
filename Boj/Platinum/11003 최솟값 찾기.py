from sys import stdin
input = stdin.readline
from collections import deque

N, L = map(int, input().split())
lst = list(map(int, input().split()))
q = deque([[lst[0],0]])

for l in range(len(lst)):
    while q and q[-1][0] > lst[l]:
        q.pop()
    while q and l - q[0][1] + 1 > L:
        q.popleft()
    q.append([lst[l],l])
    print(q[0][0],end=' ')
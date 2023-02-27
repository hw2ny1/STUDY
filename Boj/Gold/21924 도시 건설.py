import sys


def parent_check(x):
    if x != union[x]:
        union[x] = parent_check(union[x])
    return union[x]


def union_check(a,b):
    a = parent_check(a)
    b = parent_check(b)
    if a<b:
        union[b] = a
    else:
        union[a] = b


N, M = map(int, sys.stdin.readline().split())
union = [1] + [i for i in range(1,N+1)]
bridges = []
total_cost = 0
save_cost = 0
uni = []
cnt = 0

for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    bridges.append([cost, x, y])
    total_cost += cost

bridges.sort()

for bridge in bridges:
    cost, x, y = bridge
    if parent_check(x) != parent_check(y):
        union_check(x, y)
        save_cost += cost

for i in range(N+1):
    parent_check(i)
    if union[i] != 1:
        cnt += 1

if cnt > 0:
    print(-1)
else:
    print(total_cost-save_cost)
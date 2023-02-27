import sys
input = sys.stdin.readline
from math import sqrt


def parent_check(p):
    if union[p] != p:
        union[p] = parent_check(union[p])
    return union[p]


def union_check(ux, uy):
    ux = parent_check(ux)
    uy = parent_check(uy)
    if ux < uy:
        union[uy] = ux
    else:
        union[ux] = uy


N, M = map(int, input().split())
union = [i for i in range(N+1)]
node = []
path = []
for i in range(1, N+1):
    x, y = map(float, input().split())
    node.append((x, y, i))

for a in node:
    for b in node:
        x1, y1, n1 = a
        x2, y2, n2 = b
        if n1 != n2:
            temp = sqrt(pow(abs(x2-x1), 2)+pow(abs(y2-y1), 2))
            path.append((temp, n1, n2))

path.sort()

for _ in range(M):
    u1, u2 = map(int, input().split())
    union_check(u1, u2)

total_cost = 0

for cost, x, y in path:
    if parent_check(x) != parent_check(y):
        union_check(x,y)
        total_cost += cost
print(f'{round(total_cost,2):.2f}')

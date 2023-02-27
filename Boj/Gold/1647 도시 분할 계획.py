import sys

N, M = map(int,sys.stdin.readline().split())
union = [i for i in range(N+1)]
roads = []
temp = []

def parent_check(x):
    if x != union[x]:
        union[x] = parent_check(union[x])
    return union[x]


def union_check(a, b):
    a = parent_check(a)
    b = parent_check(b)
    if a < b:
        union[b] = a
    else:
        union[a] = b


for _ in range(M):
    a, b, cost = map(int,sys.stdin.readline().split())
    roads.append((cost, a, b))

roads.sort()

for road in roads:
    cost, a, b = road
    if parent_check(a) != parent_check(b):
        union_check(a, b)
        temp.append(cost)

temp.pop()
print(sum(temp))
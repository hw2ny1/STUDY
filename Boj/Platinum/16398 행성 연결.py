import sys

N = int(sys.stdin.readline())
union = [i for i in range(N+1)]
graph = [[0 for _ in range(N+1)]]
roads = []
total_cost = 0


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


for _ in range(N):
    graph.append([0]+list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1+i, N+1):
        roads.append((graph[i][j], i, j))

roads.sort()

for road in roads:
    cost, a, b = road
    if parent_check(a) != parent_check(b):
        union_check(a, b)
        total_cost += cost


print(total_cost)
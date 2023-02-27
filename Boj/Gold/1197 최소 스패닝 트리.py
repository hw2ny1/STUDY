import sys


def find_parent(x):
    if union[x] != x:
        union[x] = find_parent(union[x])
    return union[x]


def union_parent(A, B):
    A = find_parent(A)
    B = find_parent(B)
    if A < B:
        union[B] = A
    else:
        union[A] = B


node_num, M = map(int, sys.stdin.readline().split())
nodes = []
union = [i for i in range(node_num+1)]
total_cost = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes.append((c, a, b))

nodes.sort()

for node in nodes:
    cost, a, b = node
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        total_cost += cost

print(total_cost)
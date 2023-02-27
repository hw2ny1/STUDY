def parent(x):
    if x != uni[x]:
        uni[x] = parent(uni[x])
    return uni[x]

def union(a,b):
    a = parent(a)
    b = parent(b)
    if a < b:
        uni[b] = a
    else:
        uni[a] = b

N = int(input())
M = int(input())
nodes = []
uni = [i for i in range(N+1)]
total_cost = 0

for i in range(M):
    a,b,c = map(int,input().split())
    nodes.append((c,a,b))

nodes.sort()

for node in nodes:
    cost,a,b = node
    if parent(a) != parent(b):
        union(a,b)
        total_cost += cost

print(total_cost)
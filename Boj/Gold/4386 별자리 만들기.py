import sys
input = sys.stdin.readline


def parent_check(x):
    if union[x] != x:
        union[x] = parent_check(union[x])
    return union[x]


def union_check(cx,cy):
    cx = parent_check(cx)
    cy = parent_check(cy)
    if cx < cy:
        union[cx] = cy
    else:
        union[cy] = cx


N = int(input())
star = [];links = [];union = [i for i in range(N+1)];total = 0
for i in range(1,N+1):
    x, y = map(float,input().split())
    star.append((i,x,y))

for node1, x1, y1 in star:
    for node2, x2, y2 in star:
        if node1 != node2:
            temp = pow(pow(x2-x1,2) + pow(y2-y1,2),0.5)
            links.append((temp, node1, node2))

links.sort()
for cost, x, y in links:
    if parent_check(x) != parent_check(y):
        union_check(x,y)
        total += cost

print('%0.2f' % total)

import sys
input = sys.stdin.readline


def parent_check(p):
    if union[p] != p:
        union[p] = parent_check(union[p])
    return union[p]


def union_check(uni_x,uni_y):
    uni_x = parent_check(uni_x)
    uni_y = parent_check(uni_y)
    if union[uni_x] < union[uni_y]:
        union[uni_y] = uni_x
    else:
        union[uni_x] = uni_y


N = int(input())
planet_x = []
planet_y = []
planet_z = []
links = []
union = [u for u in range(N)]
total_cost = 0

for num in range(N):
    x, y, z = map(int, input().split())
    planet_x.append((x, num))
    planet_y.append((y, num))
    planet_z.append((z, num))

planet_x.sort();planet_y.sort();planet_z.sort()

for planet in planet_x, planet_y, planet_z:
    for i in range(N-1):
        cost_a, a = planet[i]
        cost_b, b = planet[i+1]
        links.append((abs(cost_b - cost_a), a, b))

links.sort()

for link in links:
    cost, x, y = link
    if parent_check(x) != parent_check(y):
        union_check(x, y)
        total_cost += cost

print(total_cost)
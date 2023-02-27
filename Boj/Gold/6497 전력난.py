import sys


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


while True:
    house_num, road_num = map(int, sys.stdin.readline().split())
    if house_num == 0 and road_num == 0:
        break

    union = [i for i in range(house_num)]
    roads = []
    total_cost, cost_save = 0, 0
    for _ in range(road_num):
        a, b, cost = map(int, sys.stdin.readline().split())
        roads.append((cost, a, b))
        total_cost += cost

    roads.sort()

    for road in roads:
        cost, a, b = road
        if parent_check(a) != parent_check(b):
            union_check(a, b)
            cost_save += cost

    print(total_cost - cost_save)

import sys
input = sys.stdin.readline


def parent_check(p):
    if union[p] != p:
        union[p] = parent_check(union[p])
    return union[p]


def union_check(uni_x, uni_y):
    uni_x = parent_check(uni_x)
    uni_y = parent_check(uni_y)
    if uni_x < uni_y:
        union[uni_y] = uni_x
    else:
        union[uni_x] = uni_y


school_num, road_num = map(int,input().split())
school_gender = ['N'] + list(map(str,input().split()))
union = [i for i in range(school_num+1)]
roads = []
total_cost = 0

for _ in range(road_num):
    x, y, cost = map(int, input().split())
    if school_gender[x] == school_gender[y]:
        continue
    roads.append((cost,x,y))

roads.sort()

for road in roads:
    cost, x, y = road
    if parent_check(x) != parent_check(y):
        union_check(x, y)
        total_cost += cost

for i in range(school_num+1):
    parent_check(i)

union = list(set(union))
if len(union) > 2:
    print(-1)
else:
    print(total_cost)
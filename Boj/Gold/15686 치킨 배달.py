from itertools import *


def cost(A, B):
    x1, y1 = A
    x2, y2 = B
    return abs(x1-x2) + abs(y1-y2)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
total_cost = 1e8
history = []

for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            house.append([x, y])
        if city[x][y] == 2:
            chicken.append([x, y])

history = list(combinations(chicken,M))


for chicken_tmep in history:
    temp_1 = []
    for hou in house:
        temp = []
        for chi_temp in chicken_tmep:
            temp.append(cost(hou, chi_temp))
        temp_1.append(min(temp))
    total_cost = min(sum(temp_1), total_cost)

print(total_cost)

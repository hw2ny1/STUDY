import copy
import sys
from collections import deque
from itertools import *


def search():
    global virus
    for x in range(len(graph_original)):
        for y in range(len(graph_original[x])):
            if graph_original[x][y] == 2:
                virus.append([x, y])
            elif graph_original[x][y] == 0:
                wall.append([x, y])


def spread(virus):
    global graph
    virus_temp = copy.deepcopy(virus)
    while virus_temp:
        x, y = virus_temp.popleft()
        graph[x][y] = 2
        if x > 0 and graph[x-1][y] == 0:
            virus_temp.append([x-1, y])
        if row-1 > x and graph[x+1][y] == 0:
            virus_temp.append([x+1, y])
        if y > 0 and graph[x][y-1] == 0:
            virus_temp.append([x, y-1])
        if com-1 > y and graph[x][y+1] == 0:
            virus_temp.append([x, y+1])


def check_virus(graph):
    temp = 0
    for grap in graph:
        temp += grap.count(0)
    return temp


row, com = map(int, sys.stdin.readline().split())
graph_original = []
virus = deque([])
wall = []
safe_zone = 0

for _ in range(row):
    graph_original.append(list(map(int, sys.stdin.readline().split())))

search()
wall = deque(list((combinations(wall,3))))

while wall:
    walls = wall.popleft()
    graph = copy.deepcopy(graph_original)
    for zone in walls:
        x, y = zone
        graph[x][y] = 1
    spread(virus)
    safe_zone = max(safe_zone, check_virus(graph))

print(safe_zone)

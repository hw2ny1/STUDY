import sys
import heapq
input = sys.stdin.readline


def parent_check(p):
    if p != union[p]:
        union[p] = parent_check(union[p])
    return union[p]


def union_check(uni_x, uni_y):
    uni_x = parent_check(uni_x)
    uni_y = parent_check(uni_y)
    if union[uni_x] < union[uni_y]:
        union[uni_y] = uni_x
    else:
        union[uni_x] = uni_y


def DFS(start, now, val):
    for next_, next_cost in links[now]:
        if not visited[next_]:
            visited[next_] = True
            max_line_cost[start][next_] = max(val, next_cost)
            DFS(start, next_, max_line_cost[start][next_])


student_num, line_num = map(int,input().split())
max_line_cost = [[0 for _ in range(student_num+1)] for _ in range(student_num+1)]
union = [i for i in range(student_num + 1)]
links = [[] for _ in range(student_num+1)]
lines = []

for _ in range(line_num):
    x, y, cost = map(int, input().split())
    heapq.heappush(lines, (cost, x, y))

cnt = 0
total_cost = 0
while lines:
    cost, x, y = heapq.heappop(lines)
    if parent_check(x) != parent_check(y):
        links[x].append([y, cost])
        links[y].append([x, cost])
        union_check(x, y)
        total_cost += cost
        cnt += 1
        if cnt == student_num-1:
            break

for i in range(1,student_num+1):
    visited = [False for _ in range(student_num+1)]
    DFS(i,i,0)

Q_num = int(input())
for _ in range(Q_num):
    x, y = map(int, input().split())
    print(total_cost - max_line_cost[x][y])
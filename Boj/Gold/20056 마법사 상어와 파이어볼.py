from sys import stdin
from collections import deque
input = stdin.readline

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])


def move(r, c, s, d):
    nr = (r + dx[d]*s)%N
    nc = (c + dy[d]*s)%N
    return nr, nc


def merge():
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                fire_volt = deque()
                while graph[i][j]:
                    fire_volt.append(graph[i][j].pop())
                num_of_fire = len(fire_volt)
                mass_of_fire = 0
                speed_of_fire = 0
                flag_a, flag_b, cnt = 0, 0, 0
                for m, s, d in fire_volt:
                    cnt += 1
                    mass_of_fire += m
                    speed_of_fire += s
                    if d%2:
                        flag_a += 1
                    else:
                        flag_b += 1
                mass_of_fire = int(mass_of_fire/5)
                speed_of_fire = int(speed_of_fire/num_of_fire)
                if mass_of_fire != 0:
                    if flag_a == cnt or flag_b == cnt:
                        for k in [0,2,4,6]:
                            graph[i][j].append([mass_of_fire, speed_of_fire, k])
                    else:
                        for k in [1,3,5,7]:
                            graph[i][j].append([mass_of_fire, speed_of_fire, k])


def check_fire():
    temp = []
    for i in range(N):
        for j in range(N):
            while graph[i][j]:
                m, s, d = graph[i][j].pop()
                temp.append((i, j, m, s, d))
    while temp:
        r, c, m, s, d = temp.pop()
        nr, nc = move(r, c, s, d)
        graph[nr][nc].append([m, s, d])


while K:
    K -= 1
    check_fire()
    merge()


fire = deque()
for i in range(N):
    for j in range(N):
        while graph[i][j]:
            fire.append(graph[i][j].pop())

ans = 0
for m,s,d in fire:
    ans += m
print(ans)
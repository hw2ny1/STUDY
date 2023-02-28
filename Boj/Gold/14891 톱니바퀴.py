def turn(gear_num, way):
    global gear
    visited[gear_num] = True
    for dx in [1, -1]:
        nx = gear_num + dx
        if nx < 0 or 4 <= nx:continue
        if dx == 1:
            if gear[gear_num][2] != gear[nx][6] and not visited[nx]:
                turn(nx, -way)
        if dx == -1:
            if gear[gear_num][6] != gear[nx][2] and not visited[nx]:
                turn(nx, -way)
    if way == 1:
        gear[gear_num] = gear[gear_num][-1] + gear[gear_num][:-1]
    elif way == -1:
        gear[gear_num] = gear[gear_num][1:] + gear[gear_num][0]


import sys
input = sys.stdin.readline
gear = [input().strip() for _ in range(4)]
K = int(input())

for _ in range(K):
    num, dire = map(int, input().split())
    visited = [False] * 4
    turn(num-1, dire)

ans = 0
for i in range(4):
    if gear[i][0] == '1':
        ans += pow(2,i)
print(ans)


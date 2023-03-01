import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0];dy = [0, 0, -1, 1]
row, col, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(row)]
aircon = []
for i in range(row):
    if room[i][0] == -1:
        aircon.append(i)


def diffusion():
    room_temp = []
    q = []
    for i in range(row):
        for j in range(col):
            if room[i][j] > 0:
                q.append((i,j))
    while q:
        x, y = q.pop()
        temp = int((room[x][y]/5))
        temp_n = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or row <= nx or ny < 0 or col <= ny:continue
            if room[nx][ny] == -1:continue
            room_temp.append((nx, ny, temp))
            temp_n += 1
        room[x][y] -= temp_n*temp

    while room_temp:
        x, y, temp = room_temp.pop()
        room[x][y] += temp


def air_condition_re(air_x, air_y):
    x = air_x-1
    y = air_y
    room[air_x-1][air_y] = 0
    while x-1 >= 0:
        room[x][y] = room[x-1][y]
        x -= 1
    while y + 1 < col:
        room[x][y] = room[x][y + 1]
        y += 1
    while x < air_x:
        room[x][y] = room[x + 1][y]
        x += 1
    while y-1 > air_y:
        room[x][y] = room[x][y-1]
        y -= 1
    room[air_x][air_y + 1] = 0


def air_condition(air_x, air_y):
    x = air_x+1
    y = air_y
    room[air_x+1][air_y] = 0
    while x+1 < row:
        room[x][y] = room[x+1][y]
        x += 1
    while y+1 < col:
        room[x][y] = room[x][y+1]
        y += 1
    while x > air_x:
        room[x][y] = room[x-1][y]
        x -= 1
    while y-1 > air_y:
        room[x][y] = room[x][y-1]
        y -= 1
    room[air_x][air_y + 1] = 0


while t:
    diffusion()
    air_condition_re(aircon[0], 0)
    air_condition(aircon[1], 0)
    t-=1

ans = 0
for r in room:
    ans += sum(r)

print(ans+2)


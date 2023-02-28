import sys
input = sys.stdin.readline

view = [(-1, 0), (0, 1), (1, 0), (0, -1)]

row, col = map(int, input().split())
ro_r, ro_c, ro_vi = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(row)]
ans = 0
priority = 1


def promising(x,y):
    for dx, dy in view:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= row or ny < 0 or ny >= col:continue
        if room[nx][ny] != 0:continue
        return True
    return False


while True:
    # for ro in room:
    #     print(*ro)
    # print('--------------------------')
    if priority == 1:
        if room[ro_r][ro_c] == 0:
            room[ro_r][ro_c] = 2
            ans += 1
        if promising(ro_r, ro_c):
            priority = 3
        else:
            priority = 2

    if priority == 2:
        dx, dy = view[ro_vi]
        if room[ro_r-dx][ro_c-dy] == 1:
            print(ans)
            break
        else:
            ro_r -= dx
            ro_c -= dy
            priority = 1

    if priority == 3:
        while True:
            ro_vi = (ro_vi - 1) % 4
            dx, dy = view[ro_vi]
            if room[ro_r+dx][ro_c+dy] == 0:
                ro_r += dx
                ro_c += dy
                priority = 1
                break



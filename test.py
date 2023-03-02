import sys
from collections import deque
input = sys.stdin.readline
dire = [(-1, 0), (1, 0), (0, 1), (0, -1)]
row, col, N = map(int, input().split())
fishing_king_point = 0
total = 0
shark = deque()
pool = [[0 for _ in range(col+1)] for _ in range(row+1)]
for _ in range(N):
    r, c, s, d, z = map(int, input().split())
    shark.append([r, c])
    pool[r][c] = [s, d-1, z]


def fishing_king():
    global fishing_king_point, total
    fishing_king_point += 1
    for i in range(row + 1):
        if pool[i][fishing_king_point]:
            total += pool[i][fishing_king_point][2]
            pool[i][fishing_king_point] = 0
            return


def shark_move():
    pass


while fishing_king_point != col:
    fishing_king()
    shark_move()
    for po in pool:
        print(po)
    print('---------------------')

print(total)
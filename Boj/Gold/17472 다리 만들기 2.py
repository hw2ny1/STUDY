import sys
from collections import deque
input = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]

# BFS로 섬마다 번호를 붙임
def bfs(x,y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = True
    zido[x][y] = cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if zido[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    zido[nx][ny] = cnt
                    q.append((nx,ny))

# land 에서 end 섬까지 최소 다리길이를 계산
def check_bridge(land,end):
    q = deque([])
    count = sys.maxsize
    for i in range(row):
        for j in range(col):
            if zido[i][j] == land:
                q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if zido[nx][ny] == 0:
                    temp = 0
                    while 0 <= nx < row and 0 <= ny < col:
                        if zido[nx][ny] == end and temp >= 2:
                            count = min(count, temp)
                            break
                        if zido[nx][ny] > 0:
                            temp = sys.maxsize
                            break
                        nx += dx[i]
                        ny += dy[i]
                        temp += 1
    return count

# 크루스칼 알고리즘을 위한 parent check
def parent_check(x):
    if union[x] != x:
        union[x] = parent_check(union[x])
    return union[x]

# 크루스칼 알고리즘을 위한 union check
def union_check(x,y):
    px = parent_check(x)
    py = parent_check(y)
    if px < py:
        union[py] = px
    else:
        union[px] = py


row, col = map(int,input().split())
zido = [list(map(int,input().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
cnt = 2
links = []

# BFS 알고리즘을 이용하여 섬마다 번호를 붙임 2번부터 시작
for i in range(row):
    for j in range(col):
        if zido[i][j] == 1:
            bfs(i,j)
            cnt += 1

# 다리의 최소길이를 알아내어 list에 넣음
for i in range(2,cnt):
    for j in range(2,cnt):
        if i != j:
            links.append((check_bridge(i,j),i,j))

# 리스트 정렬
links.sort() #우선순위 큐 안쓰고 sort() 쓰니까 넘어감..

union = [i for i in range(cnt)]
visited = [i for i in range(cnt)]
total_cost = 0

#크루스칼 알고리즘
for cost, x, y in links:
    if cost < sys.maxsize:
        if parent_check(x) != parent_check(y):
            # print(f'{x-1}에서 {y-1}로 가는 {cost}')
            union_check(x,y)
            total_cost += cost

# 한번더 체크 안해주니 틀리더라
for i in range(cnt):
    union[i] = parent_check(i)

# 유니온 파운드를 이용하여 전부다 연결되었는지 확인
union = set(union)
if total_cost > 1e8 or len(union) != 3:
    print(-1)
else:
    print(total_cost)
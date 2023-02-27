from collections import deque

# 방향벡터
dir = [(1,0),(-1,0),(0,1),(0,-1)]

# 유망한지 확인
def promising(nx, ny, color):
    if 0 > nx or nx > 11 or 0 > ny or ny > 5:
        return False
    if sit[nx][ny] != color:
        return False
    return True

# 너비우선 탐색
def bfs(x, y, color, visited):
    # temp : 같은 색 뿌요를 담기 위한 리스트
    temp = []
    visited[x][y] = True
    q = deque([(x,y)])
    # 근처에 있는 뿌요 수 체크
    while q:
        x,y = q.popleft()
        temp.append((x,y))
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if promising(nx,ny,color) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
    # 뿌요가 4개 이상 모여있다면 터트리기
    if len(temp) >= 4:
        while temp:
            x, y = temp.pop()
            sit[x][y] = '.'
        return True
    return False

# 뿌요마다 터트릴 수 있는지 체크
def puyo_pop():
    visited = [[False for _ in range(6)] for _ in range(12)]
    # 뿌요가 터졌는지 확인하기 위한 flag
    flag = 0
    for i in range(12):
        for j in range(6):
            if sit[i][j] != '.' and not visited[i][j]:
                if bfs(i, j, sit[i][j],visited):
                    flag += 1
    return flag

# 뿌요가 터진 후 아래로 정렬하기
def puyo_down():
    for j in range(5, -1, -1):
        for i in range(11,-1,-1):
            # 뿌요의 자신 아래에 빈 공간이 있으면 끝 혹은 다른 뿌요가 있는 곳까지 이동
            if sit[i][j] != '.':
                row = i
                while True:
                    if row >= 11 or sit[row+1][j] != '.':
                        break
                    if sit[row+1][j] == '.':
                        sit[row+1][j],sit[row][j] = sit[row][j],sit[row+1][j]
                    row += 1


sit = [list(input()) for _ in range(12)]
cnt = 0
# 뿌요연쇄가 이어진다면 계속 반복
while True:
    if puyo_pop():
        puyo_down()
    else:
        break
    cnt += 1
# 뿌요가 연쇄된 횟수
print(cnt)

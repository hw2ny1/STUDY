# 리스트 앞에서 pop하기 위한 deque 모듈 사용
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(start_node):
    global cnt
    cnt += 1
    queue = deque([])
    queue.append((start_node[0],start_node[1]))
    while queue:
        x,y = queue.pop()
        graph[x][y] = 0
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
                if graph[x+dx[i]][y+dy[i]] == 1:
                    queue.append((x+dx[i],y+dy[i]))

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        y,x = map(int,input().split())
        graph[x][y] = 1
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                BFS((x,y))
    print(cnt)
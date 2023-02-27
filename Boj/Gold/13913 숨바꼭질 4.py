from collections import deque
import sys
input = sys.stdin.readline

inf = 100001

def route(end):
    result = []
    temp = end
    for _ in range(visited[end]+1):
        result.append(temp)
        temp = path[temp]
    return result[::-1]

def DFS(start,end):
    visited[start] = 0
    q = deque([start])

    while q:
        via = q.popleft()
        if end == via:
            print(visited[end])
            print(*route(end))
            break
        for i in (via*2,via-1,via+1):
            if inf > i >= 0:
                if visited[i] == -1:
                    visited[i] = visited[via] + 1
                    path[i] = via
                    q.append(i)

start, end = map(int,input().split())
visited = [-1 for _ in range(inf)]
path = [0]*inf
DFS(start,end)
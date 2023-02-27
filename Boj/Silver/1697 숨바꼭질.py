from collections import deque

def BFS(start,end):
    visit = [0] * inf
    q = deque([start])
    while q:
        temp = q.popleft()
        if temp == end:
            return visit[end]
        for via in (temp-1,temp+1,temp*2):
            if via >= 0 and via < inf and not visit[via]:
                visit[via] = visit[temp] + 1
                q.append(via)

inf = 100001
a,b = map(int,input().split())
print(BFS(a,b))
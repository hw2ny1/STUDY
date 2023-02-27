import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []
meet = []
for _ in range(N):
    a,b,c = map(int,input().split())
    q.append((b,c))

q.sort(key=lambda x: (x[0],x[1]))
while q:
    x,y = heapq.heappop(q)
    if not meet:
        heapq.heappush(meet,y)
        continue
    if meet[0] <= x:
        heapq.heappop(meet)
        heapq.heappush(meet,y)
    else:
        heapq.heappush(meet,y)
print(len(meet))
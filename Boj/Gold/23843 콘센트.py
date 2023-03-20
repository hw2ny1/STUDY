import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
con = []
time = 0

while arr:
    while arr and len(con) < M:
        heapq.heappush(con,time + arr.pop())
    while arr and con[0] < time:
        heapq.heappop(con)
        heapq.heappush(con,time + arr.pop() - 1)
    time += 1

print(max(con))
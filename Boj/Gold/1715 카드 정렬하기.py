import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    heapq.heappush(q,int(input()))

result = 0
while N != 1:
    card1 = heapq.heappop(q)
    card2 = heapq.heappop(q)
    result += (card1 + card2)
    heapq.heappush(q,card1+card2)
    N -= 1
print(result)
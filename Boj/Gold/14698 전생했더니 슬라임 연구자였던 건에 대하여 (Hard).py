import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    q = list(map(int,input().split()))
    heapq.heapify(q)
    result = 1
    while N != 1:
        card1 = heapq.heappop(q)
        card2 = heapq.heappop(q)
        result = result * (card1 * card2)
        heapq.heappush(q,card1*card2)
        N -= 1
    print(result%1000000007)
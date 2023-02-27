from collections import deque

N = int(input())
card = deque([i for i in range(1, N+1)])

while N != 1:
    card.popleft()
    card.append(card.popleft())
    N -= 1

print(*card)
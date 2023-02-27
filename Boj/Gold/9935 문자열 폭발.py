import sys
from collections import deque
input = sys.stdin.readline

string = deque(list(input().strip()))
boom = list(input().strip())
result = []
bo = len(boom)
n = 0
for _ in range(len(string)+1):
    if result[-bo:] == boom:
        for _ in range(bo):
            result.pop()
            continue
    if string:
        result.append(string.popleft())
if result:
    print(''.join(result))
else:
    print('FRULA')
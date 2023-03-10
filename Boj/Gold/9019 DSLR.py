import sys
input = sys.stdin.readline
from collections import deque

def D(x):
    return (x*2)%10000

def S(x):
    return 9999 if x == 0 else x-1

def L(x):
    return (x*10+x//1000)%10000

def R(x):
    return (x%10)*1000 + x//10

N = int(input())
for _ in range(N):
    a, b = map(int,input().split())

    q = deque([(a,'')])
    s = set()
    while q:
        now, his = q.popleft()
        if now == b:
            print(his)
            break
        if now not in s:
            q.append((D(now), his + 'D'))
            q.append((R(now), his + 'R'))
            q.append((L(now), his + 'L'))
            q.append((S(now), his + 'S'))
            s.add(now)
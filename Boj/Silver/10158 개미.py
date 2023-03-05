from sys import stdin
input = stdin.readline
from collections import deque

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t)//w
b = (q + t)//h

if a%2:
    np = w - (p + t)%w
else:
    np = (p + t)%w
if b%2:
    nq = h - (q + t)%h
else:
    nq = (q + t)%h

print(np,nq)
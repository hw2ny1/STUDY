import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def parents_check(x):
    if union[x] != x:
        union[x] = parents_check(union[x])
    return union[x]

def union_check(x,y,inx):
    global ans
    x = parents_check(x)
    y = parents_check(y)
    if x != y:
        union[max(x,y)] = min(x,y)
    elif ans == 0:
        ans = inx

n, m = map(int,input().split())
union = [i for i in range(n)]
ans = 0

for i in range(m):
    a, b = map(int,input().split())
    union_check(a,b,i+1)
    if ans:
        break

print(ans)

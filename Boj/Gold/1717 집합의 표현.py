import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def parent_check(p):
    if p != union[p]:
        union[p] = parent_check(union[p])
    return union[p]


def union_check(p, q):
    p = parent_check(p)
    q = parent_check(q)
    if union[p] < union[q]:
        union[q] = p
    else:
        union[p] = q


N, M = map(int, input().split())
union = [i for i in range(N+1)]
for _ in range(M):
    flag, a, b = map(int,input().split())
    if not flag:
        union_check(a, b)
    else:
        if parent_check(a) == parent_check(b):
            print('YES')
        else:
            print('NO')
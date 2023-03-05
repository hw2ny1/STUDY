import sys
input = sys.stdin.readline

N, M = map(int,input().split())
z = sorted(list(map(int,input().split())))
z.sort()
his = []


def back(now):
    if len(his) == M:
        print(*his)
        return
    for i in range(now,N):
        if z[i] not in his:
            his.append(z[i])
            back(i+1)
            his.pop()


back(0)
def ugly(n):
    re = 1
    n2, n3, n5 = [], [], []
    for _ in range(n-1):
        n2 += [re*2]
        n3 += [re*3]
        n5 += [re*5]
        re = min(n2[0], n3[0], n5[0])
        if re == n2[0]:
            del n2[0]
        if re == n3[0]:
            del n3[0]
        if re == n5[0]:
            del n5[0]
    return re

n = int(input())
N = list(map(int,input().split()))
for i in N:
    print(ugly(i),end=' ')
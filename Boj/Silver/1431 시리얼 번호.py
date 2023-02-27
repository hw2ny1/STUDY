import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    temp = input().rstrip()
    som = 0
    temp2 = list(temp)
    for te in temp:
        if 48 <= int(ord(te)) <= 57:
            som += int(te)
    lst.append((len(temp),som,temp))
lst.sort()
for z,s,ls in lst:
    print(ls)

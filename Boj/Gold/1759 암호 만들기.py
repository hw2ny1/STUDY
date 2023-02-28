import sys
input = sys.stdin.readline

L, C = map(int,input().split())
alph = list(map(str,input().split()))
alph.sort()
ans = ''
def back(cnt,start):
    global ans
    if cnt == L:
        mo, ja = 0, 0
        for a in ans:
            if a in ('a','e','i','o','u'):
                mo += 1
            else:
                ja += 1
        if mo >=1 and ja >= 2:
            print(ans)
        return
    for i in range(start,C):
        if alph[i] not in ans:
            ans += alph[i]
            back(cnt + 1,i)
            ans = ans[:-1]
back(0,0)
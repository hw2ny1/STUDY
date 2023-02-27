n = int(input())
s = list(map(str,input().split()))
cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        temp = s[i] + s[j]
        if temp == 'HITSMUSIC':
            cnt += 1

print(cnt)
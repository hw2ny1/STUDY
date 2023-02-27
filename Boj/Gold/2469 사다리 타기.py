def alph(x):
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    temp = temp[:x]
    return temp

import sys
input = sys.stdin.readline

K = int(input())
n = int(input())
up = list(alph(K))
down = list(input().strip())

ladder = []
for _ in range(n):
    ladder.append(list(input().strip()))

for i in range(n):
    if ladder[i][0] == '?':
        break
    for j in range(K-1):
        if ladder[i][j] == '-':
            up[j], up[j+1] = up[j+1], up[j]

for i in range(n-1,-1,-1):
    if ladder[i][0] == '?':
        break
    for j in range(K-1):
        if ladder[i][j] == '-':
            down[j], down[j+1] = down[j+1], down[j]

result = ['*' for _ in range(K-1)]

for k in range(K-1):
    if up[k] == down[k+1] and down[k+1] == up[k]:
        result[k] = '-'
        up[k],up[k+1] = up[k+1],up[k]

if up == down:
    print(''.join(result))
else:
    print('x'*(K-1))

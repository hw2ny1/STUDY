import sys
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    a,b = map(int,input().split())
    meeting.append([a,b,b-a])

meeting.sort(key=lambda x: (x[1],x[0]))
cnt = 0
now = -1

for x,y,z in meeting:
    if now <= x:
        now = y
        cnt += 1
print(cnt)
import sys
input = sys.stdin.readline

H, L = map(int, input().split())
wall = list(map(int, input().split()))+[0]
rain = 0;L_max = wall[0];R_max = max(wall)
for i in range(1, L):
    if L_max-wall[i] > 0 and R_max - wall[i] > 0:
        rain += min(L_max-wall[i], R_max - wall[i])
    if wall[i] > L_max:L_max = wall[i]
    if wall[i] == R_max:R_max = max(wall[i+1:L+1])
print(rain)

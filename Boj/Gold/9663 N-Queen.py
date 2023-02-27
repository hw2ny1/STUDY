def promising(x, zz):
    for j in range(x):
        if chess[x] == chess[j] or abs(zz - chess[j]) == abs(x - j):
            return False
    return True


def backtracking(cnt):
    global total
    if cnt == N:
        total += 1
        return
    else:
        for i in range(N):
            chess[cnt] = i
            if promising(cnt, i):
                backtracking(cnt+1)


N = int(input())
chess = [100 for _ in range(N)]
total = 0

backtracking(0)

print(total)
def num():
    if len(history) == N:
        print(*history)
        return
    for i in range(1,M+1):
        history.append(i)
        num()
        history.pop()

M, N = map(int,input().split())
history = []
num()
def numlist():
    if len(history) == M:
        print(*history)
    for i in range(1,N+1):
        if i not in history:
            history.append(i)
            numlist()
            history.pop()

N,M = map(int,input().split())
history = []
numlist()
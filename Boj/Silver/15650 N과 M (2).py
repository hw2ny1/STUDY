def numlist(start):
    global result
    if len(history) == M:
        print(*history)
    for i in range(start,N+1):
        if i not in history:
            history.append(i)
            numlist(i+1)
            history.pop()

N,M = map(int,input().split())
history = []
numlist(1)

def num(start):
    if len(history) == M:
        print(*history)
        return
    for i in range(start,N+1):
        history.append(i)
        num(i)
        history.pop()
        
N,M = map(int,input().split())
history = []
num(1)
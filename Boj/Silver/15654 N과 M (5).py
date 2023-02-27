def nums(start):
    if len(history) == M:
        print(*history)
        return
    for i in num:
        if i not in history:
            history.append(i)
            nums(i)
            history.pop()
        
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
history = []
nums(1)
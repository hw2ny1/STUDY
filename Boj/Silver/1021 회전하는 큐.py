from collections import deque

N, M = map(int, input().split());cnt = 0
queue = deque([i for i in range(1,N+1)])
a = deque(list(map(int,input().split())))
while a:
    if queue[0] == a[0]:
        queue.popleft()
        a.popleft()
    else:
        cnt += 1
        if queue.index(a[0]) <= len(queue)//2:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
print(cnt)


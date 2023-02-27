from collections import deque

clock = deque([12,9,3,6])

rotate = int(int(input())/90)

def BFS(clock, rotate):
    temp = 0
    while rotate:
        clock.appendleft(clock.pop())
        temp = clock.pop()
        clock.appendleft(clock.pop())
        clock.append(temp)
        rotate -= 1
    print(*clock)

BFS(clock, rotate)
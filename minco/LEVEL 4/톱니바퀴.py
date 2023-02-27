from collections import deque

gear = [deque([3,7,4]),deque([2,6,9]),deque([5,1,2]),deque([3,6,7])]

def turn_gear(gear,turn_n):
    for i in range(4):
        while turn_n[i]:
            turn_n[i] -= 1
            gear[i].appendleft(gear[i].pop())
    for i in range(3):
        for j in range(4):
            print(gear[j][i],end='')
        print('')

turn = list(map(int,input().split()))
turn_gear(gear,turn)
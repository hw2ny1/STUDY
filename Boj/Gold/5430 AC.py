import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    rd = input().strip()
    N = int(input())
    test = input().strip()[1:-1]
    k = 1
    cnt = 0
    molu = 1
    
    if test == '':
        test = deque()
    else:
        test = deque(test.split(','))
        
    rd = rd.replace('RR','')
    
    for i in rd:
        if i == 'R':
            cnt += 1
            if k == 1:
                k = -1
            else:
                k = 1
        elif i == 'D' and test:
            if k == 1:
                test.popleft()
            if k == -1:
                test.pop()
        else:
            molu = 0
    if cnt % 2 == 1:
        test.reverse()
    if molu:
        print('['+','.join(test)+']')
    else:
        print('error')
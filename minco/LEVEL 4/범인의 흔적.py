from collections import deque

evidence = [[-1,8],
            [0,3],
            [0,5],
            [1,6],
            [2,8],
            [4,9],
            [4,10]]

def dfs(evidence,startnode,path):
    path.append(startnode)
    if evidence[startnode][0] != 0:
        startnode = evidence[startnode][0]
        dfs(evidence,startnode,path)
        print(f'{startnode}번index({evidence[startnode][1]}시)')
    elif evidence[startnode][0] == 0:
        print('0번index(출발)')
    
def dfs_2(evidence,N,path):
    dfs(evidence,N,path)
    print(f'{N}번index({evidence[N][1]}시)')

path = deque([])
N = int(input())

dfs_2(evidence,N,path)
ground = [0,0,0,0,0]

def DFS(ground,node,age):  
    if node >= 5 or age == 0:
        print('_____')
        return
    ground[node] = age
    for i in range(5):
        if ground[i] > 0:
            print(age,end = '')
        elif ground[i] == 0:
            print('_',end = '')
    print('')
    ground[node] = 0
    DFS(ground,node+1,age-1)

N,M = map(int,input().split())
DFS(ground,N,M)
    
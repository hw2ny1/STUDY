bridge = ['시작',3,1,2,1,3,2,1,2,1,'도착']

N = int(input())
path = []

def dfs(bridge,start_node,path,N):
    path.append(bridge[start_node])
    if bridge[start_node] != '도착':
        start_node += N
        N = bridge[start_node]
        dfs(bridge,start_node,path,N)
    elif bridge[start_node] == '도착':
        print(*path,end=' ')
        for i in range(len(path)-2,-1,-1):
            print(path[i],end=' ')

dfs(bridge,0,path,N)
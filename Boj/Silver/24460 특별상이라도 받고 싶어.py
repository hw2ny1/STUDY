def slice(x,y,n):
    if n ==1:
        return graph[x][y]
    else:
        List = [slice(x,y,n//2),slice(x,y+n//2,n//2),slice(x+n//2,y,n//2),slice(x+n//2,y+n//2,n//2)]
        List.sort()
        return List[1]

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

print(slice(0,0,N))
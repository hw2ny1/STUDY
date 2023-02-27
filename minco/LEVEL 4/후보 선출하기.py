lista = list(map(str,input()))
N = int(input())

def vote(lista,path,N):
    if len(path) == N:
        print(path)
        return
    for i in range(len(lista)):
        path += lista[i]
        vote(lista,path,N)
        path = path[:-1]

path = ''
vote(lista,path,N)
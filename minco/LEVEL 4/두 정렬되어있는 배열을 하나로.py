list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

def DFS(lista,listb,i,j):
    if i == len(lista) and j == len(listb):
        return
    elif i == len(lista):
        print(listb[j],end=" ")
        DFS(lista,listb,i,j+1)
    elif j == len(listb):
        print(lista[i],end=" ")
        DFS(lista,listb,i+1,j)
    if i <len(lista) and j <len(listb):
        if lista[i] < listb[j]:
            print(lista[i],end=" ")
            DFS(lista,listb,i+1,j)
        elif lista[i] > listb[j]:
            print(listb[j],end=" ")
            DFS(lista,listb,i,j+1)
        else:
            print(lista[i],listb[j],end = ' ')
            DFS(lista,listb,i+1,j+1)

i,j = 0,0
DFS(list_a,list_b,i,j)
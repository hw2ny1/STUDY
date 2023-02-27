node = ['A','B','C','D','E','F','G','H','I','J']
P = [0,0,0,3,3,3,6,6,8,8]

def alph(x):
    alphabet = 'ABCDEFGHIJK'
    return alphabet[x]

def Union(a,b):
    if P[node.index(b)] != P[node.index(a)]:
        P[node.index(b)] = P[node.index(a)]
    return

def Find(x,start_x):
    if node.index(alph(x)) == P[x]:
        P[start_x] = P[x]
    else:
        Find(P[x],start_x)

N = int(input())

for _ in range(N):
    a,b = map(str,input().split())
    Union(a,b)

for i in range(8):
    Find(i,i)

P = list(set(P))
print(f'{len(P)}개')
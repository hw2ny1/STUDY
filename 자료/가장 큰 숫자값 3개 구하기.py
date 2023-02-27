<<<<<<< HEAD
def maxx(arr,s):
    M = []
    for a in range(len(arr)):
        for b in range(len(arr[a])):
            M.append(arr[a][b])
    M = list(set(M))
    M.sort(reverse=True)
    return M[s-1]
        

        
#def acount(arr,s):
#    p = 0
#    for i in range(len(arr)):
#        p += arr[i].count(s)
#    return p

def where(arr,width,s):
    for i in range(width):
        try:
            if arr[i].count(s) > 0:
                return("(%d,%d)"%(i,arr[i].index(s)))
        except:
            break
        
a,b = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(a)]

for i in range(1,4):
    print("%s%s"%(maxx(A,i),where(A,a,maxx(A,i))))

=======
def maxx(arr,s):
    M = []
    for a in range(len(arr)):
        for b in range(len(arr[a])):
            M.append(arr[a][b])
    M = list(set(M))
    M.sort(reverse=True)
    return M[s-1]
        

        
#def acount(arr,s):
#    p = 0
#    for i in range(len(arr)):
#        p += arr[i].count(s)
#    return p

def where(arr,width,s):
    for i in range(width):
        try:
            if arr[i].count(s) > 0:
                return("(%d,%d)"%(i,arr[i].index(s)))
        except:
            break
        
a,b = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(a)]

for i in range(1,4):
    print("%s%s"%(maxx(A,i),where(A,a,maxx(A,i))))

>>>>>>> 0070b05758edd0c2e3ee96913c6f59c766664669

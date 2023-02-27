def f(i, k, s, t):
# i원소, k 집합의크기, s i-1까지
    global cnt
    if i == k:
        if s==t:
            cnt +=1
        return
    else:
        f(i+1, k, s+A[i],t)
        f(i+1, k, s, t)
    
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
cnt = 0
bit = [0]*N

f(0,N,0,key)
print(cnt)
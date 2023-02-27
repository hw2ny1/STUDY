brother = list(map(int,input().split()))

path = 0
count = 0
def dfs(brother,path,level):
    global count
    if level >= 5:
        if path >= 10 and path <= 20:
            count += 1
        else:
            return
    else:
        dfs(brother,path+brother[level],level+1)
        dfs(brother,path,level+1)

dfs(brother,path,0)
print(count)
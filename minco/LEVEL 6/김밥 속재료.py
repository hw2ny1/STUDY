alph = list(input())
result = ''
def dfs(alph,result,cnt = 0):
    if cnt == 3:
        print(result)
        return
    for i in alph:
        result += i
        dfs(alph,result,cnt+1)
        result = result[:-1]
dfs(alph,result)
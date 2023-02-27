map = [[3,2,1,3,2,'테러범',1],['R','R','L','R','L','테러범','L']]

n = int(input())

def dfs(map,n):
    if map[0][n] == '테러범':
        print(f'{n}번')
    elif map[1][n] == 'R':
        dfs(map,n+map[0][n])
        print(f'{n}번')
    else:
        dfs(map,n-map[0][n])
        print(f'{n}번')

dfs(map,n)
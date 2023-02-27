chance = int(input())

number = range(51)
m,n = 0,50
for _ in range(chance):
    num,updo = input().split()
    num = int(num)
    if updo == 'UP':
        m = max(m,num)
    elif updo == 'DOWN':
        n = min(n,num)

if m - n == 2 or n - m ==2:
    print(int((m+n)/2))
elif n <  m :
    print('ERROR')
else:
    print(f'{m+1} ~ {n-1}')

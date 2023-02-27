words = ['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']
temp, cnt = 0, 0

serch = list(str(input()))
serch_2 = []
result = []
result.extend(words)

for i in range(len(serch)):
    if serch[i] != '?':
        serch_2.append((i,serch[i]))

for i in range(len(words)):
    for n,m in serch_2:
        if result[i][n] != m:
            result[i] = '0000'

while result.count('0000') > 0:
    result.remove('0000')

print(len(result))

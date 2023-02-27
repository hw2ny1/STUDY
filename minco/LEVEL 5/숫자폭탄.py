N = int(input())
numlist = list(map(int,input().split()))

for i in range(N-2):
    if numlist[i] == numlist[i+1] and numlist[i] == numlist[i+2] and numlist[i] > 0:
        numlist[i] = ''
        numlist[i+1] = ''
        numlist[i+2] = ''

while numlist.count('')>0:
    numlist.remove('')

numlist.sort()

for i in range(len(numlist)):
    print(numlist[i],end=' ')
n = int(input())
gold = list(map(int,input().split()))

result = []

def find_position(gold,N):
    new_gold = list(map(int,gold))
    left = 0
    right = len(new_gold)-1
    while left <= right:
        mid = (left+right)//2
        if N == new_gold[mid]:
            break
        elif N > new_gold[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return mid

while gold:
    gold.sort(reverse=True)
    cnt = 0
    poket = []
    for _ in range(2):
        temp = gold.pop()
        if type(temp) == float:
            break
        else:
            cnt += 1
            poket.append(temp)
    if len(poket) >= 1:
        result.extend(poket)
    if cnt != 2:
        break
    elif cnt == 2:
        gold.insert(find_position(gold,temp*2),float(temp*2))

print(len(result))
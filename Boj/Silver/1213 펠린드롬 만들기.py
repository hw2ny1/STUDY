string = input()
arr = [0] * 100
for s in string:
    arr[ord(s)] += 1
N = sum(arr)
flag = []
for i in range(100):
    if arr[i] % 2:
        flag.append([i,arr[i]])
if (N%2 and len(flag) != 1) or (not N%2 and len(flag) > 0):
    print('I\'m Sorry Hansoo')
else:
    ans = ''
    for i in range(100):
        if arr[i]:
            temp = arr[i]//2
            arr[i] -= temp
            ans += chr(i)*temp

    if flag:
        ans += chr(flag[0][0])
        arr[flag[0][0]] -= 1

    for i in range(99,-1,-1):
        if arr[i]:
            ans += chr(i)*arr[i]
    print(ans)
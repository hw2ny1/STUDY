isp = {'+':1,'-':1,'*':2,'/':2,'(':0}
icp = {'+':1,'-':1,'*':2,'/':2,'(':3}

string = input().strip()
stack = []
for str in string:
    if str == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            else:
                print(temp, end='')
    else:
        if ord(str) > 60:
            print(str, end='')
        else:
            if not stack or icp[str] > isp[stack[-1]]:
                stack.append(str)
            else:
                while True:
                    if not stack or icp[str] > isp[stack[-1]]:
                        break
                    print(stack.pop(),end='')
                stack.append(str)
while stack:
    print(stack.pop(), end='')
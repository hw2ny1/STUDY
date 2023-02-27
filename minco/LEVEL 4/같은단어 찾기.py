str1 = str(input())
str2 = str(input())

N = len(str2)
max_length = 0
max_lengword = ''
while N:
    for i in range(N-1):
        for j in range(N):
            temp = str2[i:i+j]
            if str1.find(temp) >= 0:
                max_length = max(max_length,len(temp))
                if len(temp) >= len(max_lengword): 
                    max_lengword = temp
    N -= 1
print(max_length)
print(max_lengword)
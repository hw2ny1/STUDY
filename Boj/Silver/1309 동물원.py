N = int(input())
temp_1 = 3
temp_2 = 7
temp_3 = 0
if N == 1:
    print(temp_1)
elif N == 2:
    print(temp_2)
else:
    while N-2:
        temp_3 = (temp_2*2 + temp_1)%9901
        temp_1 = temp_2
        temp_2 = temp_3
        N -= 1
    print(temp_3)
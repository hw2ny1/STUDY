from collections import deque

number = [str(input()) for _ in range(3)]

def compare(number):
    n = len(number)
    while n != 1:
        temp = 0
        if len(number[n-1]) < len(number[n-2]):
            number.pop()
        elif len(number[n-1]) > len(number[n-2]):
            temp = number.pop()
            number.pop()
            number.append(temp)
        else:
            i = 0
            while len(number[n-1])-i:
                if number[n-1][i] == number[n-2][i]:
                    pass
                else:
                    if number[n-1][i] > number[n-2][i]:
                        temp = number.pop()
                        number.pop()
                        number.append(temp)
                        break
                    else:
                        number.pop()
                        break
                i+=1
        n -= 1
    print(*number)

compare(number)
N = int(input())
book_list = list(map(str,input().split()))
book_list.sort()

def binary_Serch(book,book_list):
    left = 0
    right = len(book_list)-1
    cnt = 0
    while left <= right:
        mid = (left + right)//2
        if book == book_list[mid]:
            break
        elif book_list[mid] > book:
            right = mid-1
        else:
            left = mid+1
        cnt += 1
    
    if book_list[mid] == book:
        if cnt < int(second):
            print('pass')
        else:
            print('fail')
    else:
        print('fail')

M = int(input())
for _ in range(M):
    book, second = input().split()
    binary_Serch(book,book_list)
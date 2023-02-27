card = list(str(input()))
N = int(input())

card_list = card[-7:-1]
print(max(card_list,key=card_list.count))
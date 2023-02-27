words = list(input().split('_'))

while words.count('')>0:
    words.remove('')

for i in range(len(words)):
    print(f'{i+1}#{words[i]}')
s = list(input())

for i in range(len(s)-1):
    if s[i] == '(' and s[i+1] =='(':
        s[i] = ''
    if s[i] == ')' and s[i+1] ==')':
        s[i] = ''

while s.count('')>0:
    s.remove('')

for i in range(len(s)-2):
    if s[i] == '^' and s[i+1] == '^' and s[i+2] == '^':
        s[i] = ''

while s.count('')>0:
    s.remove('')

for i in range(len(s)-2):
    if s[i] == '^' and s[i+2] == '^':
        s[i+1] = '_'

for i in range(len(s)):
    print(s[i],end='')
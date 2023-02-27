import heapq


def add_A(string):
    string = string[:-1]
    return string

def add_B(string):
    string = (string[::-1])[:-1]
    return string

S = input()
T = input()
N = 0

q = []
heapq.heappush(q,T)

while q:
    temp = heapq.heappop(q)
    if temp == S:
        N = 1
        break
    if len(temp) > len(S):
        if temp[-1] == 'A':
            heapq.heappush(q,add_A(temp))
        if temp[0] == 'B':    
            heapq.heappush(q,add_B(temp))

print(N)
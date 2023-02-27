import sys
import heapq
input = sys.stdin.readline
n,t = map(int,input().split()) # 정점의 개수 n, 간선의 수 t
train = [[] for _ in range(n)]

start,end,INF = 0,n-1,1e9
short_time = [INF]*(n)

for _ in range(t):
    a,b,w = map(int,input().split())
    train[a].append((b,w))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로(시작점은 0) 큐에 삽입
    heapq.heappush(q,(0,start))
    short_time[start]=0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (heapq 특성, 값이 작은것부터 쭉 자동 배열해줌)
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if short_time[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접합 노드들 확인
        for i in train[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더짧은 경우
            if cost < short_time[i[0]]
                short_time[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
if short_time[n-1]==INF:
    print("impossible")
else :
    print(short_time[n-1])
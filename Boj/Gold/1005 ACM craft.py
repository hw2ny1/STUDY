import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    delay = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    target = int(input().strip())


    def topology_sort():
        q = deque()
        dp = [0] * (N+1)
        for i in range(1,N+1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = delay[i]
        while q:
            now = q.popleft()
            for i in graph[now]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[now]+delay[i])
                if indegree[i] == 0:
                    q.append(i)
                if indegree[target] == 0:
                    return dp[target]
        return 0


    ans = topology_sort()
    print(ans)

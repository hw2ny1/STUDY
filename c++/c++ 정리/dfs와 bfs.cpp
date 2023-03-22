#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// index 0은 사용하지 않음으로 배열을 하나 더 추가
bool visited1[9];
bool visited2[9];
vector<int> graph[9];

void dfs(int x)
{
	visited1[x] = true;
	cout << x << " ";
	for (int i = 0; i < graph[x].size(); i++) // 인접한 노드 사이즈만큼 탐색
	{
		int y = graph[x][i];
		if (!visited1[y]) // 방문하지 않았으면 즉 visited가 False일 때 not을 해주면 True가 되므로 아래 dfs 실행
			dfs(y); // 재귀적으로 방문
	}
}

void bfs(int start) {
	queue<int> q;
	q.push(start); // 첫 노드를 queue에 삽입
	visited2[start] = true; // 첫 노드를 방문 처리

	// 큐가 빌 때까지 반복
	while (!q.empty()) {
		// 큐에서 하나의 원소를 뽑아 출력
		int x = q.front();
		q.pop();
		cout << x << ' ';
		// 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
		for (int i = 0; i < graph[x].size(); i++) {
			int y = graph[x][i];
			if (!visited2[y]) {
				q.push(y);
				visited2[y] = true;
			}
		}
	}
}

int main(void)
{
	/* 위 그래프와 동일하게 정의 */
	graph[1].push_back(2);
	graph[1].push_back(3);
	graph[1].push_back(8);

	graph[2].push_back(1);
	graph[2].push_back(7);

	graph[3].push_back(1);
	graph[3].push_back(4);
	graph[3].push_back(5);

	graph[4].push_back(3);
	graph[4].push_back(5);

	graph[5].push_back(3);
	graph[5].push_back(4);

	graph[6].push_back(7);

	graph[7].push_back(2);
	graph[7].push_back(6);
	graph[7].push_back(8);

	graph[8].push_back(1);
	graph[8].push_back(7);

	dfs(1);
	cout << endl;
	bfs(1);
}
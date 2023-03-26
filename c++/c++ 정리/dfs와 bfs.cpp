#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

vector<int> graph[1001];
int node, edge, startnode;
bool visited[1001] = { false, };

void init() {
	fill_n(visited, 1001, false);
}

void dfs(int now) {
	printf("%d%s", now, " ");
	visited[now] = true;
	for (register int i = 0; i < graph[now].size(); i++) {
		int next = graph[now][i];
		if (!visited[next]) {
			dfs(next);
		}
	}
}

void bfs(int start_node) {
	init();
	deque<int> dq = { start_node };
	visited[start_node] = true;

	while (!dq.empty()) {
		int now = dq.front();
		dq.pop_front();
		printf("%d%s", now, " ");
		for (register int i = 0; i < graph[now].size(); i++) {
			int next = graph[now][i];
			if (!visited[next]) {
				visited[next] = true;
				dq.push_back(next);
			}
		}
	}
}

int main() {
	cin >> node >> edge >> startnode;
	int a, b;

	for (register int i = 0; i < edge; i++) {
		scanf("%d%d", &a, &b);
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (register int i = 0; i <= node; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	dfs(startnode);
	cout << endl;
	bfs(startnode);
	return 0;
}
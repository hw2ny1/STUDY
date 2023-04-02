#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> p;

vector<p> g[1010];
priority_queue<int> heap[1010];
int n, m, k;

void kth_dijkstra() {
	priority_queue< p, vector<p>, greater<p> > pq;
	pq.push({ 0, 1 });
	heap[1].push(0);
	while (pq.size()) {
		int now = pq.top().second;
		int cost = pq.top().first;
		pq.pop();

		for (auto i : g[now]) {
			int nxt = i.first;
			int nxtCost = i.second + cost;
			if (heap[nxt].size() < k) {
				heap[nxt].push(nxtCost);
				pq.push({ nxtCost, nxt });
			}
			else if (heap[nxt].top() > nxtCost) {
				heap[nxt].pop();
				heap[nxt].push(nxtCost);
				pq.push({ nxtCost, nxt });
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> m >> k;
	for (int i = 0; i < m; i++) {
		int a, b, c; cin >> a >> b >> c;
		g[a].push_back({ b, c });
	}
	kth_dijkstra();

	for (int i = 1; i <= n; i++) {
		if (heap[i].size() != k) cout << "-1\n";
		else cout << heap[i].top() << "\n";
	}
}
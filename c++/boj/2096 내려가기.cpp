#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int>dp_min = {0,0,0};
	vector<int>dp_max = {0,0,0};
	vector<int>temp = { 0,0,0 };
	int now[3] = { 0,0,0 };

	for (register int i = 0; i < N; i++) {
		scanf("%d%d%d", &now[0], &now[1], &now[2]);
		temp[0] = min({ dp_min[0], dp_min[1]}) + now[0];
		temp[1] = min({ dp_min[0], dp_min[1], dp_min[2] }) + now[1];
		temp[2] = min({ dp_min[1], dp_min[2] }) + now[2];
		dp_min[0] = temp[0]; dp_min[1] = temp[1]; dp_min[2] = temp[2];

		temp[0] = max({ dp_max[0], dp_max[1] }) + now[0];
		temp[1] = max({ dp_max[0], dp_max[1], dp_max[2] }) + now[1];
		temp[2] = max({ dp_max[1], dp_max[2] }) + now[2];
		dp_max[0] = temp[0]; dp_max[1] = temp[1]; dp_max[2] = temp[2];
	}

	int max = *max_element(dp_max.begin(), dp_max.end());
	int min = *min_element(dp_min.begin(), dp_min.end());
	cout << max << " " << min;
	return 0;
}
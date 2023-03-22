#include <iostream>
#include <vector>
#include <algorithm>
#define endl '\n'
using namespace std;

void print(vector<vector<char>>& v) {
	for (auto i : v) {
		for (auto j : i) {
			cout << j;
		}
		cout << endl;
	}
}

bool promising(char namgyu, vector<vector<char>> case_,int x, int y) {
	case_[x][y] = namgyu;
	int flag;

	for (int i = 0; i < 3; i++) {
		flag = 0;
		for (int j = 0; j < 3; j++) {
			if (case_[i][j] == namgyu) {
				flag++;
			}
		}
		if (flag == 3) {
			return true;
		}
	}

	for (int i = 0; i < 3; i++) {
		flag = 0;
		for (int j = 0; j < 3; j++) {
			if (case_[j][i] == namgyu) {
				flag++;
			}
		}
		if (flag == 3) {
			return true;
		}
	}

	if (case_[1][1] == namgyu and case_[0][0] == case_[1][1] and case_[1][1] == case_[2][2]) {
		return true;
	}

	if (case_[1][1] == namgyu and case_[2][0] == case_[1][1] and case_[1][1] == case_[0][2]) {
		return true;
	}

	return false;
}

int tictectoe(int tc) {
	vector<vector<char>> case_(3,vector<char>(3,'0'));
	vector<pair<int, int>> q;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> case_[i][j];
			if (case_[i][j] == '-') {
				q.push_back({ i,j });
			}
		}
	}
	char namgyu;
	cin >> namgyu;
	int temp = q.size();
	for (int k = 0; k < temp; k++) {
		if (promising(namgyu, case_, q.back().first, q.back().second)) {
			cout << "Case " << tc << ':' << endl;
			case_[q.back().first][q.back().second] = namgyu;
			print(case_);
			return 0;
		}
		q.pop_back();
	}
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		tictectoe(i+1);
	}
}
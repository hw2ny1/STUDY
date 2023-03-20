#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


void print(vector<int> &v) {
	/*
	함수에서 인수를 가져올 때 주소로 가져오는 듯.
	*/
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

int main(void) {
	vector<int> vec;
	for (int i = 110; i > 64; i--) {
		vec.push_back(i);
	}
	print(vec);
	/*
	sort(시작 주소, 끝 주소, 함수 ex(greater<int>(), less<int>() 등등))
	*/
	sort(vec.begin(), vec.end());
	print(vec);

	return 0;
}
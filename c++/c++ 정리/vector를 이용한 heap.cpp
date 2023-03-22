#include <iostream>
#include <vector>
#include <algorithm>
#define endl '\n'
using namespace std;

void print(vector<int> &v) {
	for (auto i:v) {
		cout << i << " ";
	}
	cout << endl;
}

int main(void) {
	vector<int> v(vector<int> {1, 6, 5, 2, 3, 8, 4, 9, 7});
	print(v);

	/*
	최대 힙
	*/
	make_heap(v.begin(), v.end());
	print(v);

	/*
	최소 힙
	*/
	vector<int> v2(vector<int> {1, 6, 5, 2, 3, 8, 4, 9, 7});
	print(v);

	make_heap(v2.begin(), v2.end(), greater<>{});
	print(v2);

	/*
	push_heap 이나 pop_heap 할 때도 최소인지 최대인지 조건을 적어줘야함.
	*/
	pop_heap(v2.begin(), v2.end(), greater<>{});
	print(v2);
	int temp;
	temp = v2.back();
	cout << temp << endl;
	v2.pop_back();
	print(v2);

	pop_heap(v2.begin(), v2.end(), greater<>{});
	print(v2);
	temp = v2.back();
	cout << temp << endl;
	v2.pop_back();
	print(v2);
}
#include <iostream>
#include <deque>
using namespace std;

void print(deque<int> &v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

int main(void) {
	deque<int> dq;
	/*
	덱에 뒤에서 추가, 앞에 추가 O(1)로 가능
		push_back, push_front
	덱에 뒤에서 제거, 앞에 제거 O(1)로 가능
		pop_back, pop_front
	*/
	dq.push_back(7);
	dq.push_front(3);
	
	/*
	덱 사이에 삽입도 가능하다.
	*/
	dq.insert(dq.begin() + 1, 5);

	/*
	덱에 접근할때 at과 []가 있는데 at은 오류, []은 쓰레기값이 나온다.
	*/
	dq[1] = 9;
	
	print(dq);
}
#include <iostream>
#include <list>
using namespace std;

int main() {
	//list 초기화
	list<int> list1;
	
	//list 4개의 3으로 초기화
	list<int> list2(4, 0);

	//리스트에 append appendleft
	list1.push_front(1);
	list2.push_back(2);

	//리스트에 pop popleft 근데 삭제만 함 리턴X
	list1.pop_front();
	list2.pop_back();
	
	//insert 삽입
	//list1.insert(cur, temp);

	//erase 가리키는값 삭제하기그리고 그 위치를 반환
	//cur = list1.erase(cur);

	list<int> a = {1,2,3,4,5,6,7,8,9,10};
	for (list<int>::iterator iter = a.begin(); iter != a.end(); iter++)
		cout << *iter << endl;
	
	
	list<int> temp1;
	list<int> temp2;
	for (int i = 0; i < 10; i++) {
		temp1.push_back(i);
	}

	for (int i = 11; i < 20; i++) {
		temp2.push_back(i);
	}
	//temp2을 temp1뒤에 붙임
	temp1.merge(temp2);

	list<int>::iterator iter = temp1.begin();
	//temp1의 head를 가리키는 포인터를 4만큼 이동
	advance(iter, 4);

	return 0;
}
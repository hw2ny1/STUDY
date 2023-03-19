#include <iostream>
#include <deque>
using namespace std;
int main(){
	//int 자료형을 저장하는 동적배열 생성
	deque<int> dq;
	//배열 맨 앞에 원소(5) 추가
	dq.push_front(5);
	//배열 맨 뒤에 원소(5) 추가
	dq.push_back(5);
	//배열 맨 앞의 원소 삭제
	dq.pop_front();
	//배열 맨 뒤의 원소 삭제
	dq.pop_back();
	//나머지는 vector와 동일하다.
	return 0;
}
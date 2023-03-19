#include <iostream>
#include <utility>
using namespace std;
int main(){
	//int, int 자료형을 저장하는 변수 선언
	pair<int, int=""> p;
	//(4, 5)를 p에 저장
	p=make_pair(4, 5);
	//c++11부터 가능
	p={4, 5};
	return 0;
}
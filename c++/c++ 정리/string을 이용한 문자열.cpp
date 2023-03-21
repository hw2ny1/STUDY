#include <iostream>
#include <string>
#define endl "\n"
using namespace std;

int main()
{
	/*
	문자열 초기화, 파이썬처럼 조회 가능.
	front 와 back으로 앞, 뒤 문자 조회 가능.
	length로 길이 확인. size와 동일.
	resize 사용시 남는공간을 특정 문자로 채울 수 있음.
	empty 비었는지 확인.
	find 문자열 중 찾기
	push_back, pop_back 맨뒤 문자열 추가 제거.
	*/
	string str;
	cin >> str;
	cout << str[4] << endl;

	cout << str.front() << str.back() << endl;

	cout << str.length();

	str.resize(20, 'Z');
	cout << str;
}
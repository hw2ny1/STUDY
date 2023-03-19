#include <iostream>
using namespace std;

int main() {
	int a,b,c;
	/*
	scanf 이  cin 보다 더 빠르다
	scanf는 readline처럼 whitespace도 같이 받는다.
	scanf 뒤에는 서식문자와 주소(포인터)가 와야한다.
	%d   : char, short, int
	%ld  : long
	%lld : long long
	%f   : float,double
	%Lf  : long double
	%s   : char* 문자열
	%p   : void* 포인터의 주소 값
	%c   : 값에 대응하는 문자

	%u   : unsigned int 부호없는 10진수
	%o   : unsigned int 부호없는 8진수
	%x   : unsigned int 부호없는 16진수
	*/
	scanf("%d%d", &a, &b);
	cout << a << b << endl;
	cin >> c;
	/*
	마찬가지로 cout 보다 printf 가 빠르다.
	*/
	printf("%d%s", a,"\n");
	cout << b << c << endl;

	/*
	endl 보다 \n이 더 빠르다.
	*/
}

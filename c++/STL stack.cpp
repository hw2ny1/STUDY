#include <iostream>
#include <stack>
using namespace std;
int main(){
	//int자료형을 저장하는 스택 생성
	stack<int> st;
	//원소(4) 삽입
	st.push(4);
	//맨 위 원소 팝
	st.pop();
	//맨 위 원소 값 출력
	printf("%d\n", st.top());
	//스택이 비어있다면 1 아니면 0
	printf("%d\n", st.empty());
	//스택에 저장되어 있는 원소의 수 출력
	printf("%d\n", st.size());
	return 0;
}
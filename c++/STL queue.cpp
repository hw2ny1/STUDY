#include <iostream>
#include <queue>
using namespace std;
int main(){
	//int자료형을 저장하는 큐 생성
	queue<int> q;
	//원소(4) 삽입
	q.push(4);
	//맨 위 원소 팝
	q.pop();
	//맨 위 원소 값 출력
	printf("%d\n", q.front());
	//큐가 비어있다면 1 아니면 0
	printf("%d\n", q.empty());
	//큐에 저장되어 있는 원소의 수 출력
	printf("%d\n", q.size());
	return 0;
}
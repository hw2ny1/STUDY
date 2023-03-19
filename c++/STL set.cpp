#include <iostream>
#include <set>
using namespace std;
int main(){
	//int 자료형을 저장하는 균형잡힌 이진트리 생성
	set<int> s;
	//원소(5) 삽입
	s.insert(5);
	//6값을 가지는 원소를 찾음 있다면 해당 원소의 주소값,  없다면 s.end()리턴
	if(s.find(6)!=s.end())
		printf("존재합니다.\n");
	else
		printf("없습니다.\n");
	//저장된 원소의 수를 리턴
	printf("%d\n", s.size());
	//모든 원소 삭제
	s.clear();
	//해당 주소의 원소 삭제
	//2번째 원소 삭제
	s.erase(++s.begin());
	return 0;
}
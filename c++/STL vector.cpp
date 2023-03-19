#include <iostream>
#include <vector>
using namespace std;
int main(){
	// int 자료형을 저장하는 동적배열
	vector<int> vec1;

	//double 자료형을 저장하는 동적배열
	vector<double> vec2;

	//사용자가 정의한 Node 구조체를 저장하는 동적배열
	vector<node> vec3;

	//벡터의 초기 크기를 n으로 설정
	vector<int> vec4(n);

	//벡터의 초기 크기를 n으로 설정하고 1로 초기화
	vector<int> vec5(n, 1);

	//크기가 n*m인 2차원 벡터를 선언하고 0으로 초기화
	vector<vector<int>> vec6(n, vector<int>(m, 0));
	vector<vector<int>> v(10, vector <int>(10,0));


	//벡터의 맨 뒤에 원소(5) 추가
	vec1.push_back(5);

	//벡터의 맨 뒤 원소 삭제
	vec1.pop_back();

	//벡터의 크기 출력
	printf("%d\n", vec1.size());

	//벡터의 크기를 n으로 재설정
	vec1.resize(n);

	//벡터의 모든 원소 삭제
	vec1.clear();

	//벡터의 첫 원소의 주소, 마지막 원소의 다음 주소 리턴
	vec1.begin();
	vec1.end();

	//[a, b) 주소 구간에 해당하는 원소 삭제
	vec1.erase(vec1.begin(), vec1.end());//모든 원소 삭제
	
	//vec7은 vec1의 2번째 원소부터 마지막 원소까지 복사하여 생성
	vector<int> vec7=vector<int>(vec1.begin()+2, vec1.end());
	return 0;
}
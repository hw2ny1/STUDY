#include <iostream>
#include <vector>
using namespace std;



int main (void){
	/*
	vector는 연속적인 배열, list는 비연속적
	그래서 파이썬에서 쓰던 일반적인 list는 vector에 가깝다.

	1차원 vector 생성, 출력은 반복문으로 하나씩 출력해줘야함
	*/
	vector<int> V1;
	
	/*
	vector에 값을 추가 및 제거하는 방법
	push_back, pop_back : 맨 뒤에 우너소를 추가 및 제거, O(1)
	insert, erase : 임의 위치의 원소 추가 및 제거, O(n)
	*/

	V1.push_back(123);
	V1.pop_back();
	V1.push_back(6);

	/*
	vector 조회를 []로도 할 수 있지만, at()을 이용하거나 fron, gack도 가능하다.
	이 외에 empty로 비어있는지 확인하거나 size로 벡터 원소의 수를 반환 할 수 있다.
	*/
	V1.front();
	V1.back();

	/*
	vector 출력방법 3가지 있다.
	1. iterator
	vector<int>::iterator iter;
	for (iter = v.begin(); iter != v.end(); iter++)
	2. Random Access
	for (int i = 0; i < V.size(); i++)
	3. Range based for loop
	for (auto loop : V)
	*/
	vector<int>::iterator iter;
	for (iter = V1.begin(); iter != V1.end(); iter++) {
		cout << *iter << endl;
	}

	for (int i = 0; i < V1.size(); i++) {
		cout << V1[i] << endl;
	}

	for (auto loop : V1) {
		cout << loop << endl;
	}


	vector<vector<int>> V(10,vector<int>(10,0));
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			V[i][j] += i * j;
		}
	}

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d%s", V[i][j]," ");
		}
		cout << "\n";
	}
}
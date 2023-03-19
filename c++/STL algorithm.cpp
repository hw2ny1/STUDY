#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const int a, const int b){
	return a>b;
}

int main(){

	int arr1[100000];
	vector<int> arr2[100000];
	int n=100000;

	//sort
	//첫 원소의 주소와 마지막 원소의 다음 주소를 인자로 넘겨준다.
	sort(arr1, arr1+n);
	sort(arr2.begin(), arr2.end());
	//비교 함수도 만들어서 같이 넘겨줄 수 있다.
	sort(arr1, arr1+n, cmp);

	//stable_sort
	//사용법은 같다.
	stable_sort(arr1, arr1+n);

	//lower_bound
	//첫 원소의 주소와 마지막 원소의 다음 주소와 비교할 원소를 넘겨준다.
	//구간내의 원소들은 정렬되어 있어야한다.
	//리턴 값은 해당 원소의 주소값이다. 없다면 arr1+n을 리턴한다.
	//또는 arr2.end()를 리턴한다.
	int idx=lower_bound(arr1, arr1+n, 42)-arr1;
	printf("%d\n", idx);

	//upper_bound
	//사용법은 같다.
	vector<int>::iterator it=upper_bound(arr2.begin(), arr2.end(), 54);
	if(it!=arr2.end())
		printf("%d\n", *it);

	//max_element
	//첫 원소의 주소와 마지막 원소의 다음 주소를 인자로 넘겨준다.
	//구간내의 최대값을 가지는 원소의 주소를 리턴한다.
	printf("%d\n", *max_element(arr1, arr1+n));

	//min_element
	//사용법은 같다.
	printf("%d\n", *min_element(arr2.begin(), arr2.end()));

	//unique
	//첫 원소의 주소와 마지막 원소의 다음 주소를 인자로 넘겨준다.
	//구간내의 중복된 원소를 구간의 끝부분으로 밀어주고 마지막 원소의 다음 주소를 리턴한다.
	//구간내의 원소들은 정렬되어 있어야한다.
	//보통 erase와 함께 중복된 원소를 제거하는 방법으로 사용한다.
	arr2.erase(unique(arr2.begin(), arr2.end()), arr2.end());

	//next_permutation
	//첫 원소의 주소와 마지막 원소의 다음 주소를 인자로 넘겨준다.
	//구간내의 원소들의 다음 순열을 생성하고 true를 리턴한다.
	//다음 순열이 없다면 false를 리턴한다.
	//구간내의 원소들은 정렬되어 있어야한다.
	int arr[10];
	for(int i=0;i<10;i++)
		arr[i]=i;
	do{
		for(int i=0;i<10;i++)
			printf("%d ", arr[i]);
		printf("\n");
	}while(next_permutaion(arr, arr+10));

	return 0;
}
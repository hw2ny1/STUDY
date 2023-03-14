#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
	//헤더파일 가져와야함
	//변수 타입 먼저 지정해줘야함
	int num;
	//cin 으로 변수 input 가능
	cin >> num;
	//cout 으로 변수 출력 가능
	cout << ++num << endl;
	//switch예시
	switch (num)
	{
	case 6:
		cout << num * 2 << endl;
		break;
	case 7:
		cout << num + 5 << endl;
		break;
	}
	cout << num << endl;
	//while 예시
	int i = 0;
	while (i < num)
	{
		cout << "while 테스트" << i << "잘되고 있냐?" << endl;
		i++;
	}
	//do-while 예시
	do {
		cout << "do while" << endl;
	} while (i < num);
	//for 예시
	for (int i = 0; i < num; i++) {
		cout << i << endl;
	}
	//배열 예시
	int arr[5] = { 1,3,5,7,9 };
	//배열로 for문 예시
	for (int element : arr)
	{
		cout << element << " ";
	}
	//continue와 break
	int xnum = 2;
	for (int i = 0; i <= 100; i++)
	{
		if (i % xnum == 0)
		{
			continue;
		}
		if (i == 51)
		{
			cout << endl;
			break;
		}
		cout << i << " ";
	}
	//배열 예제
	int arrr[5] = {1,2,3,4,5};

	for (int i = 0; i < 5; i++)
	{
		arrr[i] = i;
	}
	cout << arrr << endl;
	cout << sizeof(arrr) << endl;
	cout << sizeof(arrr) / sizeof(arrr[0]) << endl;

	//2차원 배열
	int arrrr[3][4];
	
	int arr_col_len, arr_row_len;
	arr_col_len = sizeof(arrrr[0]) / sizeof(arrrr[0][0]);
	arr_row_len = (sizeof(arrrr) / arr_col_len) / sizeof(arrrr[0][0]);

	for (i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {
			arrrr[i][j] = i + j;
			cout << arrrr[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}
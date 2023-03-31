#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

int lst[1000005];

using namespace std;

void quickSort(int arr[], int start, int end) {

	int pivot = start;
	int left = pivot + 1;
	int right = end;

	if (start >= end)
		return;

	while (left <= right) {
		for (; left <= end; left++) {
			if (arr[left] > arr[pivot])
				break;
		}
		for (; right > pivot; right--) {
			if (arr[right] < arr[pivot])
				break;
		}
		if (left < right) {
			swap(arr[left], arr[right]);
		}
		else {
			swap(arr[pivot], arr[right]);
		}
	}

	quickSort(arr, start, right - 1);
	quickSort(arr, right + 1, end);

}

int main() {
	int N, t, ans;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d", &N);
		ans = N/2;
		for (register int i = 0; i < N; i++) {
			scanf("%d", &lst[i]);
		}
		
		quickSort(lst, 0, N-1);

		cout << "#" << tc << " " << lst[ans] << "\n";
	}

	return 0;
}
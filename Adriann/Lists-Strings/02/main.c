#include <stdio.h>
#include <stdlib.h>

void print_arr(int * arr, int len);
void reverse(int * arr, int len);
void swap(int * x, int * y);

int main() {
	int * arr = malloc(8 * sizeof(int));
	for(int i = 0; i < 8; i++) {
		printf("Enter number: ");
		scanf("%d", &arr[i]);
	}
	print_arr(arr, 8);
	reverse(arr, 8);
	print_arr(arr, 8);
	return 0;
}

void print_arr(int * arr, int len) {
	printf("[ ");
	for(int i = 0; i < len - 1; i++) {
		printf("%d, ", arr[i]);
	}
	printf("%d ]\n", arr[len - 1]);
}

void swap(int * x, int * y) {
	int x_val = *x;
	*x = *y;
	*y = x_val;
}

void reverse(int * arr, int len) {
	for(int i = 0; i < (len >> 1); i++) {
		swap(&arr[i], &arr[len - i - 1]);
	}
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void reverse(int * array, int size);
void swap(int * a, int * b);

int main() {
	srand(time(NULL));
	
	const int size = rand() % 16 + 1;
	int * list = malloc(size * sizeof(int));
	int range = 1000;

	printf("Generating list of %d integers between [-%d, %d]. . .\n", size, range, range);
	for(int i = 0; i < size; i++) {
		list[i] = rand() % (range + 1);
		if(rand() << 31 == 0)
			list[i] *= -1;
		printf("%d ", list[i]);
		fflush(stdout);
	}
	printf("\nReversing . . . \n");

	reverse(list, size);

	for(int i = 0; i < size; i++) {
		printf("%d ", list[i]);
	}
	printf("\n\n");

	return EXIT_SUCCESS;
}

void reverse(int * list, int size) {
	for(int i = 0; i < size / 2; i++) {
		swap(&list[i], &list[size - i - 1]);
	}
}

void swap(int * a, int * b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

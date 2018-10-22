#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int max(int * list, int size);

int main() {
	srand(time(NULL));
	
	const int size = rand() % 101;
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
	printf("\n\n\n");

	printf("Maximum value of list: %d\n", max(list, size));

	return EXIT_SUCCESS;
}

int max(int * list, int size) {
	int max = list[0];
	for(int i = 1; i < size; i++) {
		if(list[i] > max)
			max = list[i];
	}
	return max;
}

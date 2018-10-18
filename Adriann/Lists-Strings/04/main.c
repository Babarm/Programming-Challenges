#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int * data = malloc(8 * sizeof(int));
	for(int i = 0; i < 8; i++) {
		data[i] = rand() % 100;
		printf("%d ", data[i]);
	}
	printf("\n\n");

	printf("Odd Indeces: \n");
	for(int i = 0; i < 8; i+= 2) {
		printf("%d ", data[i]);
	}
	printf("\n");

	return EXIT_SUCCESS;
}

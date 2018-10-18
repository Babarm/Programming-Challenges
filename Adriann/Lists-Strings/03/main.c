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
	printf("\n");

	int test;
	printf("Please enter value: ");
	scanf("%d", &test);
	
	for(int i = 0; i < 8; i++) {
		if(data[i] == test) {
			printf("The value is in the list!\n");
			return EXIT_SUCCESS;
		}
	}
	printf("That value is not in the list!\n");
	return EXIT_SUCCESS;
}

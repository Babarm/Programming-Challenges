#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
	}


	printf("Value to check for: ");
	int value;
	int valid = scanf("%d", &value);
	while(valid != 1) {
		int gc;
		while((gc = getchar()) != EOF && gc != '\n');
		printf("That's not an integer!\n");
		printf("Value to check for: ");
		valid = scanf("%d", &value);
	}

	int found = 0;
	for(int i = 0; i < size; i++) {
		if(value == list[i]) {
			found = 1;
			break;
		}
	}
	if(found)
		printf("Value in list!\n");
	else
		printf("Value not in list!\n");

	return EXIT_SUCCESS;
}

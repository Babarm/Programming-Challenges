#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int max(int * list, int len);

int main() {
	srand(time(NULL));

	int * list = malloc(1024 * sizeof(int));
	for(int i = 0; i < 1024; i++)
		list[i] = rand();

	printf("Max of list: %d\n", max(list, 1024));

	free(list);
	return 0;
}

int max(int * list, int len) {
	int max_value = list[0];
	for(int i = 0; i < len; i++)
		if(list[i] > max_value)
			max_value = list[i];
	return max_value;
}

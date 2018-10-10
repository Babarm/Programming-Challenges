#include "main.h"

void get_id(int* id) {
	int valid, garbage_collection;

	printf("Which challenge would you like to run (ID #, 0 to quit)? ");
	valid = scanf("%d", id);

	/* Invalid input */
	while(valid != 1) {
		while((garbage_collection = getchar()) == EOF || garbage_collection == '\n');

		clear();
		printf("Which challenge would you like to run (ID #, 0 to quit)? ");
		valid = scanf("%d", id);
	}
}

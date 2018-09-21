#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

/* Method that runs the challenge code */
size_t run() {
	size_t ans = 0;

	/* +----------------------+ */
	/* | Place your code here | */
	/* +----------------------+ */
	size_t numops = 0;
	for(size_t a = 0; a < 500; a++) {
		for(size_t b = 0; b < 333; b++) {
			numops++;
			size_t c = 1000 - a - b;
			if(a * a + b * b == c * c) {
				ans = a * b * c;
			}
		}
	}

	return ans;
}

/* Main entry point for the program */
int main(int argc, char **argv) {

	/* Ready the program for number formatting */
	setlocale(LC_NUMERIC, "");

	struct timespec start, end;

	clear();

	/* Print Title of Challenge */
	printf("#9: Special Pythagorean Triplet\n");
	printf("===============================\n\n");

	printf("Running . . . \n\n");

	/* Mark the starting timestamp */
	clock_gettime(CLOCK_REALTIME, &start);
	
	/* Acquire Answer */
	size_t *ans = malloc(sizeof(size_t));
	*(ans) = run();

	/* Mark the ending timestamp and calculate time elapsed */
	clock_gettime(CLOCK_REALTIME, &end);
	long timestamp = end.tv_nsec - start.tv_nsec;

	/* Report the answer and the time taken to calculate the answer */
	printf("Answer: %'lu\n", *(ans));
	free(ans);

	/* Format the timestamp into something more readable */
	printf("Completed in ");
	if (timestamp >= 1000000000) {
		printf("%0.3f sec\n\n", (double)timestamp / 1e9);
	} else if (timestamp >= 1000000) {
		printf("%0.3f ms\n\n", (double)timestamp / 1e6);
	} else if (timestamp >= 1000) {
		printf("%0.3f \u03BCs\n\n", (double)timestamp /1e3);
	} else {
		printf("%ld ns\n\n", timestamp);
	}

	return 0;
}

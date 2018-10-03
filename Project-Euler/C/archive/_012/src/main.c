#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

size_t num_divisors(size_t val) {
	size_t limit = val;
	size_t count = 0;
	if(val == 1) { return 1; }
	for(size_t i = 1; i < limit; ++i) {
		if(val % i == 0) {
			limit = val / i;
			if(limit != i) {
				count++;
			}
			count++;
		}
	}
	return count;
}

/* Method that runs the challenge code */
size_t run() {
	size_t ans = 0;

	/* +----------------------+ */
	/* | Place your code here | */
	/* +----------------------+ */

	size_t i = 1;
	while(1) {
		ans += i;
		if(num_divisors(ans) >= 500) {
			break;
		}
		i++;
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
	printf("#12: Highly Divisible Triangular Number\n");
	printf("=======================================\n\n");

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

	if (start.tv_nsec > end.tv_nsec) { // clock underflow
		timestamp += 1000000000;
    }

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

#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

int is_prime(int val) {
	if (val == 2) { return 1; }
	if (val % 2 == 0 || val < 1) { return 0; }
	int i = 3;
	while (i * i <= val) {
		if (val % i == 0) { return 0; }
		i += 2;
	}
	return 1;
}

/* Method that runs the challenge code */
int run() {
	int ans = 0;

	/* +----------------------+ */
	/* | Place your code here | */
	/* +----------------------+ */
	int count = 1, prime = 1;
	do {
		prime += 2;
		if(is_prime(prime)) {
			count++;
			if(count == 10001) {
				break;
			}
		}
	} while (1);

	ans = prime;

	return ans;
}

/* Main entry point for the program */
int main(int argc, char **argv) {

	/* Ready the program for number formatting */
	setlocale(LC_NUMERIC, "");

	struct timespec start, end;

	clear();

	/* Print Title of Challenge */
	printf("#7: 10 001st Prime\n");
	printf("==================\n\n");

	printf("Running . . . \n\n");

	/* Mark the starting timestamp */
	clock_gettime(CLOCK_REALTIME, &start);
	
	/* Acquire Answer */
	int *ans = malloc(sizeof(int));
	*(ans) = run();

	/* Mark the ending timestamp and calculate time elapsed */
	clock_gettime(CLOCK_REALTIME, &end);
	long timestamp = end.tv_nsec - start.tv_nsec;

	/* Report the answer and the time taken to calculate the answer */
	printf("Answer: %'d\n", *(ans));
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

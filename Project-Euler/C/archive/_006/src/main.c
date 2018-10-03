#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

int abs(val) {
	if (val < 0) {
		return val * -1;
	}
	return val;
}

/* Method that runs the challenge code */
int run() {
	int ans = 0;

	/* +----------------------+ */
	/* | Place your code here | */
	/* +----------------------+ */
	int square_sum = 0, sum_square = 0;
	for (int i = 0; i <= 100; i++) {
		square_sum += i;
	}
	square_sum *= square_sum;

	for (int i = 0; i <= 100; i++) {
		sum_square += (i * i);
	}

	ans = abs(square_sum - sum_square);

	return ans;
}

/* Main entry point for the program */
int main(int argc, char **argv) {

	/* Ready the program for number formatting */
	setlocale(LC_NUMERIC, "");

	struct timespec start, end;

	clear();

	/* Print Title of Challenge */
	printf("#6: Sum Square Difference\n");
	printf("=========================\n\n");

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

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

	int length = 52;

	/* initialize an int array to hold sums of digits for later arithmetic */
	int digit_sums[length];
	for(int i = 0; i < length; i++) { digit_sums[i] = 0; }

	/* read data file line by line, but don't store in memory */
	FILE * file_pointer = fopen("data.txt", "r");
	char * line = malloc(length * sizeof(char));
	while(fgets(line, length, file_pointer) != NULL) {
		for(int i = 0; i < length - 2; i++) {
			digit_sums[i] += (line[i] - '0');
		}
	}

	/* free memory occupied by file_pointer and line */
	free(file_pointer);
	free(line);

	/* shift all values down 2 spots, as the newline and null characters are not needed */
	for(int i = length - 3; i >= 0; i--) {
		digit_sums[i + 2] = digit_sums[i];
		digit_sums[i] = 0;
	}

	/* collapse all the digit sums (finish the addition) */
	for(int i = length - 1; i > 0; i--) {
		int val = digit_sums[i] % 10;
		int carry = (digit_sums[i] - (digit_sums[i] % 10)) / 10;
		digit_sums[i - 1] += carry;
		digit_sums[i] = val;
	}
	
	/* condense the first 10 characters into ans, as specified by the challenge */
	for(int i = 0; i < 10; i++) {
		ans *= 10;
		ans += digit_sums[i];
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
	printf("#13: Large Sum\n");
	printf("==============\n\n");

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

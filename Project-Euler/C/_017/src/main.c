#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

/* Defining the size of the various words needed */
char digit_sizes[20] = {0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};
char tens_sizes[10] = {0,3,6,6,5,5,5,7,6,6};
#define HUNDRED 7
#define THOUSAND 8
#define AND 3


/* Counts the size of the word form of an integer */
/* Doesn't actually get the word form, just the size */
/* TODO: Clean up. Make it more readable, potentially more efficient */
int count_number_word_size(int val) {
	int count = 0, digit = 0, copy = val;
	if(val < 1) {
		return count;
	}
	while(copy != 0) {
		if(copy >= 1000) {
			digit = copy / 1000;
			count += digit_sizes[digit];
			count += THOUSAND;
			copy %= 1000;
		}
		if(copy >= 100) {
			digit = copy / 100;
			count += digit_sizes[digit];
			count += HUNDRED;
			copy %= 100;
			if(copy > 0) {
				count += AND;
			}
		}
		if(copy >= 20) {
			digit = copy / 10;
			count += tens_sizes[digit];
			copy %= 10;
		}
		if(copy > 0) {
			count += digit_sizes[copy];
			copy = 0;
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
	
	for(int i = 1; i <= 1000; i++) {
		ans += count_number_word_size(i);
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
	printf("#17: Number Letter Counts\n");
	printf("=========================\n\n");

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

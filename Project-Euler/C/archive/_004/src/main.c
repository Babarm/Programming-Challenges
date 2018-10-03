#include "main.h"

void clear() {
	printf("\e[1;1H\e[2J");
}

int is_palindrome(int val) {
	if(val % 10 == 0) {
		return 0;
	}
	int t, reverse = 0;
	t = val;
	while(t != 0) {
		/* Increase the decimal (allow for new ones digit) */
		reverse *= 10;

		/* Add the new ones digit */
		reverse += (t % 10);
		
		/* Remove digit from original */
		t /= 10;
	}
	return val == reverse;
}

/* Method that runs the challenge code */
int run() {
	int ans = 0;

	/* +----------------------+ */
	/* | Place your code here | */
	/* +----------------------+ */

	for (int i = 1000; i > 100; i--) {
		for (int j = 1000; j > 100; j--) {
			int k = i * j;
			if(is_palindrome(k) && k > ans) {
				/* Found the largest possible pair, as we are iterating in reverse */
				ans = k;
				break;
			}
		}
	}

	return ans;
}

/* Main entry point for the program */
/* Pretty much no reason to change the contents of this */
int main(int argc, char **argv) {

	/* Ready the program for number formatting */
	setlocale(LC_NUMERIC, "");

	struct timespec start, end;

	clear();

	/* Print Title of Challenge */
	printf("#4: Largest Palindrome Product\n");
	printf("==============================\n\n");

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

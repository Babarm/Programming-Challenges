#include <locale.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "timer.h"

void run_challenge(size_t* ans);

int main() {
	setlocale(LC_NUMERIC, "");

	// Declare the variables needed for execution
	size_t ans;
	double time_elapsed;
	uint64_t start, end;

	// Clear the screen
	printf("\e[1;1H\e[2J\n");

	// Heading for the challenge
	printf("Problem #:\n");
	printf("==========\n\n");

	// Run Problem
	run_challenge(&ans);

	// Report Answer
	printf("Answer: %'ld\n", ans);

	// Report Time Elapsed

	return EXIT_SUCCESS;
}

void run_challenge(size_t* ans) {
	*(ans) = 10000;
	return;
}

void calculate_time_elapsed(uint64_t* start, uint64_t* end, double* time_elapsed) {

}

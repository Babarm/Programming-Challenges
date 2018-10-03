/* Importing some libraries */
#include <locale.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* ==================================================================================================== */


/* Determine System so as to use proper timer */
#if defined(__linux)
#  define HAVE_POSIX_TIMER
#  include <time.h>
#  ifdef CLOCK_MONOTONIC
#    define CLOCKID CLOCK_MONOTONIC
#  else
#    define CLOCKID CLOCK_REALTIME
#  endif
#elif defined(__APPLE__)
#  define HAVE_MACH_TIMER
#  include <mach/mach_time.h>
#elif defined(_WIN32)
#  define WIN32_LEAN_AND_MEAN
#  include <windows.h>
#endif


/* ==================================================================================================== */


static uint64_t ns();
void report_time_elapsed(uint64_t* start, uint64_t* end);
void run_challenge(int64_t* ans);


/* ==================================================================================================== */


int main() {
	setlocale(LC_NUMERIC, "");

	/* Declare the variables needed for execution */
	int64_t ans;
	uint64_t start, end;

	/* Clear the screen */
	printf("\e[1;1H\e[2J\n");

	/* Heading for the challenge */
	printf("Problem #:\n");
	printf("==========\n\n");

	/* Mark starting timestamp */
	start = ns();

	/* Run Problem */
	run_challenge(&ans);

	/* Mark ending timestamp */
	end = ns();

	/* Report Answer */
	printf("Answer: %'ld\n", ans);

	/* Report Time Elapsed */
	report_time_elapsed(&start, &end);

	return EXIT_SUCCESS;
}


/* ==================================================================================================== */


/* Runs the actual code to solve the challenge */
void run_challenge(int64_t* ans) {
	int64_t val = 0x0;
	*(ans) = val;
	return;
}


/* ==================================================================================================== */


/* Format the timespan into a more readable format, and report */
void report_time_elapsed(uint64_t* start, uint64_t* end) {
	uint64_t span = *(end) - *(start);
	if(span >= 1e9) {
		printf("%'0.3f sec\n\n", (double)span / 1e9);
	} else if(span >= 1e6) {
		printf("%0.3f ms\n\n", (double)span / 1e6);
	} else if(span >= 1e3) {
		printf("%0.3f \u03BCs\n\n", (double)span / 1e3);
	} else {
		printf("%ld ns\n\n", span);
	}
	return;
}


/* ==================================================================================================== */


/* Gets the current nanosecond timestamp of the system */
static uint64_t ns() {
	static uint64_t is_init = 0;
#if defined(__APPLE__)
	static mach_timebase_info_data_t info;
	if( 0 == is_init ) {
		mach_timebase_info(&info);
		is_init = 1;
	}
	uint64_t now;
	now = mach_absolute_time();
	now *= info.numer;
	now /= info.denom;
	return now;
#elif defined(__linux)
	static struct timespec linux_rate;
	if( 0 == is_init ) {
		clock_getres(CLOCKID, &linux_rate);
		is_init = 1;
	}
	uint64_t now;
	struct timespec spec;
	clock_gettime(CLOCKID, &spec);
	now = spec.tv_sec * 1.0e9 + spec.tv_nsec;
	return now;
#elif defined(_WIN32)
	static LARGE_INTEGER win_frequency;
	if( 0 == is_init ) {
		QueryPerformanceFrequency(&win_frequency);
		is_init == 1;
	}
	LARGE_INTEGER now;
	QueryPerformanceCounter(&now);
	return (uint64_t) ((1e9 * now.QuadPart) / win_frequency.QuadPart);
#endif
}

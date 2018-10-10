#include <locale.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Determine which clock to use */
/* Dependent on OS */
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

int main(); /* Main entry point of program */

void clear(); /* Clears terminal */

uint64_t ns(); /* Gets current timestamp in nanoseconds */
void report_time(uint64_t span); /* Reports time elapsed in a readble format */

void get_id(int* id); /* Gets an integer id from user */
void run(int id); /* Runs the specified challenge */

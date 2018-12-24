#ifndef LIB
#define LIB

#include <locale.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define true 1
#define false 0

// Nanosecond Timer
#if defined(__linux)
#   define HAVE_POSIX_TIMER
#   include <time.h>
#   ifdef CLOCK_MONOTONIC
#       define CLOCK_ID CLOCK_MONOTONIC
#   else
#       define CLOCK_ID CLOCK_REALTIME
#   endif
#elif define(__APPLE__)
#   define HAVE_MACH_TIMER
#   include <mach/mach_time.h>
#elif defined(_WIN32)
#   define WIN32_LEAN_AND_MEAN
#   include <windows.h>
#endif
uint64_t ns();

// Timestamp Formatter
char * format_time(uint64_t span);

// New Method Prototypes Below
int is_prime(int n);
#endif

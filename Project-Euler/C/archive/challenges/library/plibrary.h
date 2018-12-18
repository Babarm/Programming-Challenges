#ifndef PLIB
#define PLIB

#include <locale.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define true  1
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

// Reverses an integer
int reverse_int(int n);

// Determines if an int is a palindrome
int is_palindrome_int(int n);

// Determines if a number is prime
int is_prime(int n);

// Generates a list of prime numbers below the given limit
int * prime_sieve(int limit);

// Determines the larger of two numbers
int max(int a, int b);

// Counts the number of divisors of a number
int num_divisors(int num);

// Determines the factorial of a number
double factorial(int n);

// Number of combinations (n choose k)
uint64_t C(int n, int k);

// Calculates n to the power of k
double pow(double n, double k);

// Converts an arabic number to its english representation
char * num2string(int n);

// Determines the sum of the proper divisors of a number
int sum_divisors(int n);

#endif

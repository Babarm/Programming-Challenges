#include "library.h"

int main() {
    // Allows for pretty formatting of numbers
    setlocale(LC_NUMERIC, "");

    printf("\n\n");

    // Problem Name
    printf("Problem 2: Even Fibonacci Numbers\n");
    printf("=================================\n");

    printf("Running . . .\n\n");

    // Variable to hold the answer
    uint64_t ans = 0;

    // Record the starting timestamp
    uint64_t start = ns();

    // +--------------------------+
    // | Place Problem Code Below |
    // +--------------------------+ 
    int fib = 0, a = 0, b = 1;
    while(fib <= 4000000) {
        fib = a + b;
        a = b;
        b = fib;
        if(fib % 2 == 0)
            ans += fib;
    }

    // Record the ending timestamp
    uint64_t end = ns();

    // Report answer to problem --- Must Insert Manually
    printf("Answer: %'llu\n\n", ans);

    // Format the timespan into a readable format and report
    char * timespan = format_time(end - start);
    printf("Time elapsed: %s\n\n\n", timespan);
    // Free memory used by 'timespan'
    free(timespan);

    return EXIT_SUCCESS;
}

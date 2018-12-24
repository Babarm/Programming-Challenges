#include "library.h"

int main() {
    // Allows for pretty formatting of numbers
    setlocale(LC_NUMERIC, "");

    printf("\n\n");

    // Problem Name
    printf("Problem 7: 10,001st Prime\n");
    printf("=========================\n");

    printf("Running . . .\n\n");

    // Variable to hold the answer
    uint64_t ans = 0;

    // Record the starting timestamp
    uint64_t start = ns();

    // +--------------------------+
    // | Place Problem Code Below |
    // +--------------------------+
    int count = 1;
    ans = 3;
    for(;;) {
        if(is_prime(ans))
            count++;
        if(count >= 10001)
            break;
        ans += 2;
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

#include "library.h"

int main() {
    // Allows for pretty formatting of numbers
    setlocale(LC_NUMERIC, "");

    printf("\n\n");

    // Problem Name
    printf("Problem 1: Multiples of 3 and 5\n");
    printf("===============================\n");

    printf("Running . . .\n\n");

    // Record the starting timestamp
    uint64_t start = ns();

    // +--------------------------+
    // | Place Problem Code Below |
    // +--------------------------+
    int p = 999 / 3;
    int ans = 3 * (p * (p + 1)) / 2;

    p = 999 / 5;
    ans += 5 * (p * (p + 1)) / 2;

    p = 999 / 15;
    ans -= 15 * (p * (p + 1)) / 2;

    // Record the ending timestamp
    uint64_t end = ns();

    // Report answer to problem --- Must Insert Manually
    printf("Answer: %'d\n\n", ans);

    // Format the timespan into a readable format and report
    char * timespan = format_time(end - start);
    printf("Time elapsed: %s\n\n\n", timespan);
    // Free memory used by 'timespan'
    free(timespan);

    return EXIT_SUCCESS;
}

#include "../../library/plibrary.h"

#define LIMIT 999

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;
    uint64_t p;

    uint64_t start = ns();

    // Add all divisible by 3
    p = LIMIT / 3;
    ans += 3 * (p * (p + 1)) >> 1;

    // Add all divisible by 5
    p = LIMIT / 5;
    ans += 5 * (p * (p + 1)) >> 1;

    // Sub all divisible by 3 and 5
    p = LIMIT / 15;
    ans -= 15 * (p * (p + 1)) >> 1;

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);
    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}

#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans;

    uint64_t start = ns();

    ans = 5050 * 5050;
    int sumSquare = 0;
    for(int i = 1; i <= 100; i++) sumSquare += i * i;
    ans -= sumSquare;

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}

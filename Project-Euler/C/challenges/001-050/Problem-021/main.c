#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    uint64_t start = ns();

    for(int a = 0; a < 10000; a++) {
        int b = sum_divisors(a);
        if(a != b && a == sum_divisors(b))
            ans += a;
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
